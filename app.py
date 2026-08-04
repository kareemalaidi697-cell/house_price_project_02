from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import json
import numpy as np

app = Flask(__name__)
CORS(app)  # عشان يسمح للواجهة تتصل بالباك إند بدون أخطاء

# تحميل الموديل والأعمدة
with open('columns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']
    locations = data_columns[5:]  # المواقع بتبدأ من العمود السادس بعد الـ features الأساسية

with open('house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/get_locations', methods=['GET'])
def get_locations():
    return jsonify({'locations': locations})


@app.route('/predict_price', methods=['POST'])
def predict_price():
    try:
        # استقبال البيانات من الواجهة
        data = request.json
        location = data['location'].lower()
        bhk = int(data['bhk'])
        bath = int(data['bath'])
        carpet_area = float(data['carpet_area'])
        parking = int(data['parking'])
        floor_number = int(data['floor_number'])

        # تجهيز مصفوفة التنبؤ بنفس ترتيب الأعمدة في الموديل
        # الترتيب: bhk, bath, carpet_area, parking, floor_number, ثم المواقع
        x = np.zeros(len(data_columns))
        x[0] = bhk
        x[1] = bath
        x[2] = carpet_area
        x[3] = parking
        x[4] = floor_number

        # تفعيل العمود الخاص بالموقع المختار
        if location in data_columns:
            loc_index = data_columns.index(location)
            x[loc_index] = 1

        # التنبؤ بالسعر
        predicted_price = model.predict([x])[0]

        return jsonify({'estimated_price': round(predicted_price, 2)})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    print("🚀 بدء تشغيل خادم Flask...")
    # debug=False في بيئة الإنتاج (Render) أوفر وأأمن
    app.run(debug=False, host="0.0.0.0", port=port)

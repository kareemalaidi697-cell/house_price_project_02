# 🏠 House Price Predictor

مشروع توقع سعر العقار باستخدام Machine Learning (Linear Regression) + Flask + HTML/JS.

## 📁 محتويات المشروع

- `model_training.py` — سكريبت تدريب الموديل، بيولّد `house_price_model.pkl` و `columns.json`.
- `app.py` — سيرفر Flask (API) بيستقبل بيانات العقار ويرجّع السعر المتوقع.
- `index.html` — واجهة المستخدم.
- `requirements.txt` — المكتبات المطلوبة.
- `Procfile` — إعدادات تشغيل السيرفر على Render.

## ▶️ التشغيل محليًا

```bash
pip install -r requirements.txt
python model_training.py     # يولّد ملفات الموديل (اختياري لو already موجودة)
python app.py                 # يشغل السيرفر على http://127.0.0.1:5000
```

بعدين افتح `index.html` في المتصفح مباشرة.

## 🚀 النشر (Deployment) عشان يشتغل لايف على الإنترنت

### 1) نشر الباك إند (Flask) على Render

1. اعمل حساب على [render.com](https://render.com) (فيه خطة مجانية).
2. اربط حساب GitHub بتاعك، واختار الريبو ده.
3. من New → Web Service، اختار الريبو.
4. الإعدادات:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app` (موجودة بالفعل في `Procfile`)
5. بعد النشر هتاخد رابط زي:
   `https://your-app-name.onrender.com`

### 2) نشر الواجهة (index.html) على GitHub Pages

1. في إعدادات الريبو على GitHub: **Settings → Pages**.
2. من **Branch** اختار `main` والفولدر `/ (root)`.
3. احفظ، وهتاخد رابط زي:
   `https://your-username.github.io/repo-name/`

### 3) الربط بين الاتنين

افتح `index.html` وغيّر السطر ده في آخر الملف بالرابط اللي طلع من Render:

```js
const API_BASE = 'https://your-app-name.onrender.com';
```

واعمل commit + push تاني، وبعدها الموقع هيشتغل لايف بالكامل 🎉

> ⚠️ ملاحظة: أول طلب على Render Free tier ممكن ياخد شوية ثواني لأن السيرفر بينام لو مفيش استخدام (Cold Start)، ده طبيعي في الخطة المجانية.

## 📝 استخدام بياناتك الحقيقية

المشروع حاليًا بيستخدم بيانات وهمية صغيرة للتجربة. لو عندك ملف CSV حقيقي، افتح `model_training.py` وبدّل:

```python
df = pd.DataFrame(data)
```

بـ:

```python
df = pd.read_csv('your_data.csv')
```

وبعدين شغل `model_training.py` تاني عشان يعيد التدريب ويحدّث الملفات.

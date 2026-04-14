# 📸 Django Media Upload Project

## 📌 Overview
This project demonstrates how to upload and display media files (images) using Django.  
It covers complete media handling including file upload, storage, and rendering in the browser.

---

## 🚀 Features
- Upload images using Django forms
- Store images in the media folder
- Dynamically display uploaded images
- Clean and simple UI
- Beginner-friendly Django project

---

## 🛠️ Tech Stack
- Python
- Django
- HTML
- CSS (optional)

---

## 📂 Project Structure
```
Django-Media_url/
│
├── media/                # Stores uploaded files
├── app/
│   ├── models.py        # Image model
│   ├── views.py         # Upload & display logic
│   ├── urls.py          # App URLs
│
├── templates/
│   └── home.html        # Frontend UI
│
├── project/
│   ├── settings.py      # Media configuration
│   ├── urls.py          # Main URL routing
│
└── manage.py
```

---

## ⚙️ Media Configuration

Add this in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

## 🔗 URL Configuration

In `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # your paths
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 🔁 How It Works

1. User uploads an image from the frontend  
2. Django receives the file via `request.FILES`  
3. Image is stored in `media/uploads/`  
4. File path is saved in the database  
5. Template displays image using:

```html
<img src="{{ image.url }}">
```

---

## ▶️ Run the Project

```bash
git clone https://github.com/your-username/Django-Media_url.git
cd Django-Media_url
python manage.py runserver
```

---

## 🌐 Access the App

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 📷 Example Output
- Upload an image  
- Image appears instantly on the webpage  

---

## 📚 Learning Outcomes
- Understanding Django media files  
- Handling file uploads  
- Working with models and templates  
- Connecting frontend and backend  

---

## 👨‍💻 Author
Nithin S  

---

## ⭐ Acknowledgment
This project is built as part of learning Django Full Stack Development.

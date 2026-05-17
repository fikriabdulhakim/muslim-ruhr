# Cru Static Clone (No Database)

This Django project does not use any persistent database. All article data is stored in Python lists.

## Run locally
```bash
pip install -r requirements.txt
python manage.py runserver
```

## Deploy to Vercel
Set environment variables:
- SECRET_KEY=your-secret-key
- DEBUG=False
- ALLOWED_HOSTS=.vercel.app,your-domain.vercel.app

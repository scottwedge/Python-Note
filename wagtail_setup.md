# wagtail set up
here is the url: https://wagtail.io/developers/
```powershell
pip install wagtail
wagtail start mysite
cd mysite
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

If everything worked, http://127.0.0.1:8000 will show you a welcome page

You can now access the administrative area at http://127.0.0.1:8000/admin
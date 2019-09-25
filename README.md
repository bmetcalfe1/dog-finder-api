Steps:

1. Create virtual env (python3 -m venv my_env)
2. Run pip install -r requirements.txt
3. Add a secret key in settings.py
4. Run python manage.py runserver

To use the bonus feature (list of dogs in a given radius), pass the params latitude, longitude and radius.

Here's an example URL:
http://127.0.0.1:8000/api/dogrange?latitude=43.6532&longitude=79.3832&radius=1000
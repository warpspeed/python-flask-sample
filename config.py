import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = os.getenv('DEBUG_MODE',False)
SECRET_KEY = os.environ['SECRET_KEY']
SQLALCHEMY_DATABASE_URI = 'mysql://flask_user:password123@localhost/flask_db' + os.path.join(BASE_DIR, 'passenger_wsgi.py')

CSRF_ENABLED = True
CSRF_SESSION_KEY = SECRET_KEY

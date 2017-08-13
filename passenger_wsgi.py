from flask import Flask
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

application = Flask(__name__)
csrf.init_app(application)

application.config.from_object('config')

from app.models import Task
from app.controllers import *

if __name__ == '__main__':
    application.run(port=8000)


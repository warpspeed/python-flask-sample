from flask import Flask, render_template, request, redirect, session
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CsrfProtect

csrf = CsrfProtect()

application = Flask(__name__, static_url_path='')
csrf.init_app(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask_user:password123@localhost/flask_db'

application.config.from_object('config')

db = SQLAlchemy(application)
migrate = Migrate(application, db)

manager = Manager(application)
manager.add_command('db', MigrateCommand)

some_engine = create_engine('mysql://flask_user:password123@localhost/flask_db')

# create a configured "Session" class
Session = sessionmaker(bind=some_engine)

from app.models import Task
from app.controllers import *

if __name__ == '__main__':
    manager.run()
    application.run(port=8000)


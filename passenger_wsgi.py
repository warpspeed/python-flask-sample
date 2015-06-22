from flask import Flask, render_template, request, redirect, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CsrfProtect

csrf = CsrfProtect()

application = Flask(__name__, static_url_path='')
csrf.init_app(application)
#application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask_user:password123@localhost/flask_db'

application.config.from_object('config')

db = SQLAlchemy(application)
migrate = Migrate(application, db)

manager = Manager(application)
manager.add_command('db', MigrateCommand)

from app.controllers import *
from app.models import Task

if __name__ == '__main__':
    manager.run()
    application.run(port=8000)


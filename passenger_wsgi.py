from flask import Flask, render_template, request, redirect, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CsrfProtect

csrf = CsrfProtect()

application = Flask(__name__)
csrf.init_app(application)

application.config.from_object('config')

from app.controllers import *
from app.models import Task

if __name__ == '__main__':
    application.run(port=8000)


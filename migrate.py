from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from passenger_wsgi import application
#application = Flask(__name__)

#application.config.from_object('config')

db = SQLAlchemy(application)
migrate = Migrate(application, db)

manager = Manager(application)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

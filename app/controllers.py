from flask import Flask, render_template, request, redirect, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from passenger_wsgi import application
from app.models import Task
from config import Session

@application.route('/', methods=['GET', 'POST'])
def index():
    session = Session()
    if request.method == 'POST':
        task = Task(name=request.form['name'])
        if task.name != "":
            session.add(task)
            session.commit()
        tasks = session.query(Task).all()
        return redirect('/')
    else:
        tasks = session.query(Task).all()
        return render_template('index.html', tasks=tasks)

@application.route('/clear-complete/', methods=['POST'])
def clear_complete():
    session = Session()
    if request.method == 'POST':
        for task in session.query(Task).filter_by(is_complete=True).all():
            if (task.is_complete):
                session.delete(task)
        session.commit()
    return redirect('/')

@application.route('/<int:task_id>/toggle-complete/', methods=['POST'])
def toggle_complete(task_id):
    session = Session()
    if request.method == 'POST':
        task = session.query(Task).filter_by(id=task_id).all()[0]
        task.is_complete = not task.is_complete
        session.commit()
        return redirect('/')
    return redirect('/')

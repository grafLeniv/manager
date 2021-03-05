from app import db
from datetime import datetime
from flask_login import UserMixin
import re


#col_task = db.Table('col_task',
#					db.Column('col_id', db.Integer, db.ForeignKey('col.id')),
#					db.Column('task_id', db.Integer, db.ForeignKey('task.id'))
#	)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<User %r>' % self.username


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.Text)
    dtcreated = db.Column(db.Date)
    col_id = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)

#    cols = db.relationship('Col', secondary=col_task, backref=db.backref('tasks', lazy='dynamic'))


    def __repr__(self):
        return '<Task id: {}, name: {}>'.format(self.id, self.name)



class Col(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)

    def __init__(self, *args, **kwargs):
        super(Col, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<Col id: {}, title: {}>'.format(self.id, self.title)
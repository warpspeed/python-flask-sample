from migrate import db

class Task(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    is_complete = db.Column(db.Boolean)

    def __init__(self, name):
        self.name = name
        self.is_complete = False

    def __repr__(self):
        return '<Task %r>' % self.name

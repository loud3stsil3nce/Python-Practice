from . import db
from flask_login import UserMixin, login_manager
from sqlalchemy.sql import func

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(1000))
    task_description = db.Column(db.String(1000))
    status = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
@login_manager.user_loader
def get_user(ident):
  return User.query.get(int(ident))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    tasks = db.relationship('Task')
    
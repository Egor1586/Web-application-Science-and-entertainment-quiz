from flask_login import UserMixin

from Project.database import db

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(20), nullable= True)
    email = db.Column(db.String(50), nullable= True)
    password = db.Column(db.String(20), nullable= True)
    password_confirmation = db.Column(db.String(20), nullable= True)
    is_teacher = db.Column(db.Boolean)
    is_admin= db.Column(db.Boolean, default= 0)

    def __repr__(self):
        return f'User: {self.name}'
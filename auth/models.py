from flask_login import UserMixin

from Project.settings import db

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(20), nullable= True)
    email = db.Column(db.String(50), nullable= True)
    password = db.Column(db.String(20), nullable= True)
    password_confirmation = db.Column(db.String(20), nullable= True)
    is_teacher = db.Column(db.Boolean)
    is_certified = db.Column(db.Boolean)

    def __repr__(self):
        return f'User: {self.name}'
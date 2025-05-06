from Project.database import db
from sqlalchemy.dialects.postgresql import ARRAY

class Test(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    topic = db.Column(db.String(100), nullable= True)
    description = db.Column(db.String(200), nullable= True)
    
    question_count = db.Column(db.Integer)
    answer_on_question = db.Column(db.Integer)
    code = db.Column(db.Integer)
    author = db.Column(db.String(100), nullable = True)

    quizes = db.relationship('Quiz', backref='test', cascade= "all, delete-orphan")
    

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String(100), nullable= True)
    
    answers = db.Column(db.String(300),  nullable= True)
    right_answer = db.Column(db.String(100),  nullable= True)

    quiz_id = db.Column(db.Integer, db.ForeignKey('test.id'))
    
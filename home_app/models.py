from Project.database import db

# class Test(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     topic = db.Column(db.String(100), nullable= True)
#     description = db.Column(db.String(200), nullable= True)
    
#     question_count = db.Column(db.Integer)
#     answer_on_question = db.Column(db.Integer)
    
#     quizes = db.relationship('Quiz', backref='quiz')
    

# class Quiz(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     question = db.Column(db.String(100), nullable= True)
    
#     answers = db.Column(db.String(300),  nullable= True)
#     right_answer = db.Column(db.String(100),  nullable= True)

#     quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    
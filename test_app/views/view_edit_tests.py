import flask
from ..models import Test, Quiz

from Project.database import db

from flask_login import current_user

def render_test_app(code):
    
    list_quiz = []
    list_answers= []

    test_id = flask.request.args.get('test_id')
    test = Test.query.filter_by(id= test_id).first()

    for quiz in Quiz.query.filter_by(quiz_id=test_id).all():
        list_answers.append(quiz.answers.split("%$№"))
        list_quiz.append(quiz)

    if flask.request.method == "POST":
        try:
            if flask.request.form['topic']:
                test.topic = flask.request.form['topic']
            
            if flask.request.form['description']:
                test.description = flask.request.form['description']
            
            db.session.commit()
        
        except:

            if flask.request.form['question']:
                print(f'{flask.request.form['question']}')
            
            for number in range(test.answer_on_question - 1):                
                if flask.request.form[f'wrong_answer{number}']:
                    print(flask.request.form[f'wrong_answer{number}'])
    

            if flask.request.form['right_answer']:
                print(flask.request.form['right_answer'])

            
    return flask.render_template(
        template_name_or_list= 'edit_test.html', 
        is_authorization = current_user.is_authenticated,
        username = current_user.username if current_user.is_authenticated else "", 
        is_teacher= current_user.is_teacher if current_user.is_authenticated else "",
        test= test,
        list_quiz= list_quiz,
        list_answers= list_answers
        )


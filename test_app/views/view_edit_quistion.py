import flask
from flask_login import current_user

from Project.database import db

from ..models import Test, Quiz

def render_edit_question(id):
    
    list_answers = []

    answer_options = " "
    correct_answer = " " 

    quiz = Quiz.query.filter_by(id = id).first()
    test = Test.query.filter_by(id = id).first()

    list_answers.append(quiz.answer_options.split("%$№"))


    if flask.request.method == 'POST':
        for number in range(test.answers_per_question):
            if number != (test.answers_per_question - 1):
                if answer_options == " ":
                    answer = flask.request.form[f'answer{number}']
                    answer_options += f'{answer}%$№'
                else:
                    answer = flask.request.form[f'answer{number}']
                    answer_options += f'%$№{answer}'
            else:
                correct_answer = flask.request.form['correct_answer']
                answer_options += f'%$№{correct_answer}'
                quiz.correct_answer = correct_answer
            
        quiz.answer_options = answer_options
        db.session.commit()
        
    return flask.render_template(
        template_name_or_list = 'edit_question.html',
        is_authorization = current_user.is_authenticated,
        username = current_user.username if current_user.is_authenticated else "",
        is_teacher= current_user.is_teacher if current_user.is_authenticated else "",
        test = test,        
        quiz = quiz,
        quiz_id = id,
        list_answers = list_answers,
        correct_answer = quiz.correct_answer
    )
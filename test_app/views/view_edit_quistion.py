import flask
from flask_login import current_user

from Project.database import db

from ..models import Test, Quiz

def render_edit_question(id):
    
    list_answers = []

    str_answer = " "
    right_answer = " " 

    quiz = Quiz.query.filter_by(id = id).first()
    test = Test.query.filter_by(id = id).first()

    list_answers.append(quiz.answers.split("%$№"))


    if flask.request.method == 'POST':
        for number in range(test.answer_on_question):
            if number != (test.answer_on_question - 1):
                print(number)
                print(test.answer_on_question)
                if str_answer == " ":
                    answer = flask.request.form[f'answer{number}']
                    str_answer += f'{answer}%$№'
                else:
                    answer = flask.request.form[f'answer{number}']
                    str_answer += f'%$№{answer}'
            else:
                right_answer = flask.request.form['right_answer']
                str_answer += f'%$№{right_answer}'
                quiz.right_answer = right_answer
                print(right_answer)
            
        quiz.answers = str_answer
        db.session.commit()
        
    return flask.render_template(
        template_name_or_list = 'edit_question.html',
        quiz = quiz,
        test = test,        
        quiz_id = id,
        is_authorization = current_user.is_authenticated,
        username = current_user.username if current_user.is_authenticated else "",
        is_teacher= current_user.is_teacher if current_user.is_authenticated else "",
        list_answers = list_answers,
        right_answer = quiz.right_answer
    )
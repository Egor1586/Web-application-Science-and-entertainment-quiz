import flask
from ..models import Test, Quiz

from flask_login import current_user


def render_test_app(code):
    answers = []
    
    list_quiz = []
    list_answers= []

    test_id = flask.request.args.get('test_id')
    test = Test.query.filter_by(id= test_id).first()

    for quiz in Quiz.query.filter_by(quiz_id = test_id).all():
        list_answers.append(quiz.answers)
        list_quiz.append(quiz)

    print(answers, type(list_answers[0]))

    return flask.render_template(
        template_name_or_list= 'test.html', 
        is_authorization = current_user.is_authenticated,
        username = current_user.name if current_user.is_authenticated else "", 
        is_teacher= current_user.is_teacher if current_user.is_authenticated else "",
        test= test,
        list_quiz= list(list_quiz),
        list_answers= list(list_answers)
        )
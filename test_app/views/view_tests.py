import flask
from ..models import Test, Quiz

from flask_login import current_user

def render_test_app(code):

    list_quiz = []
    list_answers= []

    test_id = flask.request.args.get('test_id')
    test = Test.query.filter_by(id= test_id).first()

    for quiz in Quiz.query.filter_by(quiz_id=test_id).all():
        list_answers.append(quiz.answers.split("%$№"))
        list_quiz.append(quiz)

    return flask.render_template(
        template_name_or_list= 'test.html', 
        is_authorization = current_user.is_authenticated,
        username = current_user.username if current_user.is_authenticated else "", 
        is_teacher= current_user.is_teacher if current_user.is_authenticated else "",
        test= test,
        list_quiz= list_quiz,
        list_answers= list_answers
        )


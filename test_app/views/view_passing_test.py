import flask
from ..models import Test, Quiz

from flask_login import current_user

def render_passing_test(code):
    list_quiz =[]
    list_answers= []
    list_quiz= []

    test_id = flask.request.args.get("test_id")

    test = Test.query.filter_by(id= test_id).first()

    print(test_id, test.question_count)

    for quiz in Quiz.query.filter_by(quiz_id=test_id).all():
        list_answers.append(quiz.answers.split("%$№"))
        list_quiz.append(quiz)

    if flask.request.method == "POST":
        quiz_test_id = list_quiz[0].quiz_id

        for id in range(test.question_count):
            if id != test.question_count:
                answer = flask.request.form[f'answers{quiz_test_id + id}']
                print(answer)

    return flask.render_template(
        template_name_or_list = 'passing_test.html',
        is_authorization = current_user.is_authenticated,
        username = current_user.username if current_user.is_authenticated else "", 
        is_teacher= current_user.is_teacher if current_user.is_authenticated else "",
        test = test,
        quizzes_list = list_quiz,
        list_answers= list_answers
    )
import flask
from flask_login import current_user

from ..models import Test, Quiz

def render_edit_question():
    list_my_test = []
    list_tests = Test.query.all()

    list_answers = []

    list_my_quiz = []
    list_quiz = Quiz.query.all()

    if flask.request.method == 'POST':
        for test, quiz in zip(list_tests, list_quiz):

            if test.author == current_user.username:
                first_question = flask.request.form['question1']
                second_question = flask.request.form['question2']
                third_question = flask.request.form['question3']
                fourty_question = flask.request.form['question4']
                answer = flask.request.form['answer']

                list_answers.append(first_question, second_question, third_question, fourty_question, answer)
                list_my_test.append(test)
                list_my_quiz.append(quiz)
    for question in range(list_my_test.question_count):
        for answer_on_question in range(list_my_test.answer_on_question):
            list_my_quiz[0].question = list_answers[answer_on_question]
    return flask.render_template(
        template_name_or_list = 'edit_question.html'
    )
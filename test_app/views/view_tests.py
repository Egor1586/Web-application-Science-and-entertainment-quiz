import flask
from ..models import Test, Quiz

from flask_login import current_user


def render_test_app():
    
    questions = []
    answers = []
    correct_answers = []
    len_questions = 0 

    test_id = flask.request.args.get('test_id')

    for test in Test.query.filter_by(id = test_id):
        topic = test.topic
        description  = test.description 
        question_count  = test.question_count 
        answer_on_question = test.answer_on_question
    
    for quiz in Quiz.query.filter_by(quiz_id = test_id).all():
        questions.append(quiz.question)
        answers.append(quiz.answers)
        correct_answers.append(quiz.right_answer)
        len_questions += 1

    print(f'Это количество вопросов: {len_questions}')

    return flask.render_template(
        template_name_or_list= 'test.html', 
        is_authorization = current_user.is_authenticated,
        username = current_user.name if current_user.is_authenticated else "", 
        is_teacher= current_user.is_teacher if current_user.is_authenticated else "",
        topic= topic, 
        description = description, 
        question_count = question_count, 
        answer_on_question = answer_on_question,
        count_of_tests = len_questions,
        questions = questions,
        answers = answers,
        correct_answers = correct_answers
        )
import flask
from ..models import Test, Quiz

def render_test_app():
    is_registrated = flask.session.get('is_registrated', False)
    username = flask.session.get('username')
    
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
    # len_questions = len(questions)ц
    print(f'Это количество вопросов: {len_questions}')

    return flask.render_template(
        "test.html",
        is_registrated=is_registrated, username=username, 
        is_teacher= flask.session.get("is_teacher"), 
        topic= topic, 
        description = description, 
        question_count = question_count, 
        answer_on_question = answer_on_question,
        count_of_tests = len_questions,
        questions = questions,
        answers = answers,
        correct_answers = correct_answers
        )
import flask
from home_app.models import Test
def render_test_app():
    is_registrated = flask.session.get('is_registrated', False)
    username = flask.session.get('username')
    topic = flask.session.get('')
    data= {
        "topic": "Основи Python",
        "description": "Тест на базові знання Python для початківців.",
        'count_question' : '10',
        "questions": [
            {
            "question": "Яка правильна команда для виводу тексту на екран у Python?",
            "options": [
                "echo('Hello World')",
                "console.log('Hello World')",
                "printf('Hello World')",
                "print('Hello World')"
            ],
            "correct_answer": "print('Hello World')"
            },
            {
            "question": "Який тип даних використовується для зберігання цілих чисел у Python?",
            "options": [
                "float",
                "str",
                "bool",
                "int"
            ],
            "correct_answer": "int"
            },
            {
            "question": "Як позначається початок коментаря в Python?",
            "options": [
                "//",
                "<!-- -->",
                "/* */",
                "#"
            ],
            "correct_answer": "#"
            },
            {
            "question": "Який з наведених варіантів створює список у Python?",
            "options": [
                "(1, 2, 3)",
                "{1, 2, 3}",
                "<1, 2, 3>",
                "[1, 2, 3]"
            ],
            "correct_answer": "[1, 2, 3]"
            },
            {
            "question": "Як можна отримати довжину списку у Python?",
            "options": [
                "length(list)",
                "count(list)",
                "size(list)",
                "len(list)"
            ],
            "correct_answer": "len(list)"
            }
        ]}

    test_id = flask.request.args.get('test_id')
    topic = data["topic"]
    context_data = {
    "description": data['description'],
    "count_question": data['count_question'],
    "answer_on_question": data['questions']
    }
    

    for question in data['questions']:
        print(question)


    for test in Test.query.filter_by(id = test_id):
        print(test)
        # topic = test.topic

    return flask.render_template(
        "test.html",
        is_registrated=is_registrated, username=username, 
        is_teacher= flask.session.get("is_teacher"), topic= topic, context = context_data)
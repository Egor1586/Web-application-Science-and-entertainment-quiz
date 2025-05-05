import flask
import json

from flask_login import current_user
from Project.database import db
from ..models import Test, Quiz
from ..generat_test import generate_test


def render_new_quiz():
    data= {
        "topic": "Основи Python",
        "description": "Тест на базові знання Python для початківців.",
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
        ]
        }
    
    if flask.request.method == "POST":
        try:
            topic = flask.request.form['topic']
            description = flask.request.form['description']
            count_question = flask.request.form['count_question']
            answer_on_question= flask.request.form["answer_on_question"]
            
            if not count_question:
                count_question = 10
            if not answer_on_question:
                answer_on_question = 4

            # data= generate_test(topic, description, count_question, answer_on_question)
       
            print(topic, description, count_question, answer_on_question )
            
            test = Test(
                topic= topic,
                description = description,
                question_count = int(count_question),
                answer_on_question = int(answer_on_question),
                author = current_user.name
            )

            db.session.add(test)
            db.session.commit()
            
            for quizzes in data["questions"]:
                quiz = Quiz(
                    question = quizzes["question"],
                    answers = json.dumps(quizzes["options"], ensure_ascii=False),
                    right_answer = quizzes["correct_answer"],
                    quiz_id = test.id             
                )
                db.session.add(quiz)
            
            db.session.commit()
            
            return flask.redirect(location = '/../quizzes')
        
        except:
            pass

    return flask.render_template(template_name_or_list = 'new_quiz.html',
        is_authorization = current_user.is_authenticated,
        username = current_user.name if current_user.is_authenticated else "", 
        is_teacher= current_user.is_teacher if current_user.is_authenticated else ""
        )
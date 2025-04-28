import flask
import json

# from ..models import Test, Quiz
from ..generat_test import generate_test


def render_new_quiz():
    is_registrated = flask.session.get('is_registrated', False)
    username = flask.session.get('username')
    
    if flask.request.method == "POST":
        try:
            topic = flask.request.form['topic']
            description = flask.request.form['description']
            count_question = flask.request.form['count_question']
            answer_on_question = flask.request.form["answer_on_question"]
            if not count_question:
                count_question = 10
            if not answer_on_question:
                answer_on_question = 4

            print(topic,count_question,answer_on_question)
            generate_test(topic, description, count_question, answer_on_question)
       
            # 

            options = [
                "float",
                "str",
                "bool",
                "int"
            ]
     
            json_str = json.dumps(options)

            # test = Test(
            #     topic = topic,
            #     description = description,
            #     question_count = count_question,
            #     answer_on_question = answer_on_question
            #     )
            
        except:
            pass



    return flask.render_template(template_name_or_list = 'new_quiz.html', is_registrated=is_registrated, username=username, is_teacher= flask.session.get("is_teacher"))

import flask
from flask_login import current_user
from test_app.models import Test

def render_quizzes():

    test_list = Test.query.all()
    test_id_list = []
    topic_list = []

    for test in test_list:
        if test.author == current_user.name:
            test_id_list.append(test.id)#
            topic_list.append(test.topic)

    return flask.render_template(
    template_name_or_list= 'quizzes.html', 
    is_authorization = current_user.is_authenticated,
    username = current_user.name if current_user.is_authenticated else "", 
    is_teacher= current_user.is_teacher if current_user.is_authenticated else "",
    test_id_list= test_id_list,
    topic_list= topic_list
    )


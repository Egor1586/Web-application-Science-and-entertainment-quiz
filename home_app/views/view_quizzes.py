import flask
from flask_login import current_user
from test_app.models import Test



def render_quizzes():
    list_your_test= []
    list_tests = Test.query.all()
    
    count_of_tests = 0

    for test in list_tests:
        if test.author_name == current_user.username:
            list_your_test.append(test)

    count_of_tests = int(len(list_tests))
    
    return flask.render_template(
    template_name_or_list= 'quizzes.html', 
    is_authorization = current_user.is_authenticated,
    username = current_user.username if current_user.is_authenticated else "", 
    is_teacher= current_user.is_teacher if current_user.is_authenticated else "",
    list_tests = list_your_test,
    count_of_tests = count_of_tests
    )
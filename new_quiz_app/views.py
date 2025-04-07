import flask

def render_new_quiz():
    return flask.render_template(template_name_or_list = 'quiz.html')
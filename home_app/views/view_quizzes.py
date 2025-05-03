import flask

def render_quizzes():
    is_registrated = flask.session.get('is_registrated', False)
    username = flask.session.get('username')

    print(flask.session.get("is_teacher"))
    return flask.render_template(template_name_or_list= 'quizzes.html', is_registrated=is_registrated, username=username, is_teacher= flask.session.get("is_teacher"), )
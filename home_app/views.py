import flask

# flags = ['is_registrated']
# context = {flag: flask.session.get(flag, False) for flag in flags}
# name = flask.session.get('name')

def render_home():
    is_registrated = flask.session.get('is_registrated', False)
    username = flask.session.get('username')

    print(username)

    return flask.render_template(template_name_or_list= 'home.html', is_registrated=is_registrated, username=username)


def render_score():
    is_registrated = flask.session.get('is_registrated', False)
    username = flask.session.get('username')
    
    return flask.render_template(template_name_or_list= 'score.html', is_registrated=is_registrated, username=username)


def render_profile():
    is_registrated = flask.session.get('is_registrated', False)
    username = flask.session.get('username')

    return flask.render_template(template_name_or_list= 'profile.html', is_registrated=is_registrated, username=username)


def render_new_quiz():
    is_registrated = flask.session.get('is_registrated', False)
    username = flask.session.get('username')

    return flask.render_template(template_name_or_list = 'quiz.html', is_registrated=is_registrated, username=username)

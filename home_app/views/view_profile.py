import flask

def render_profile():
    is_registrated = flask.session.get('is_registrated', False)
    username = flask.session.get('username')

    return flask.render_template(template_name_or_list= 'profile.html', is_registrated=is_registrated, username=username, is_teacher= flask.session.get("is_teacher"))
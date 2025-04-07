import flask

def render_profile_app():
    return flask.render_template(template_name_or_list= 'profile.html')
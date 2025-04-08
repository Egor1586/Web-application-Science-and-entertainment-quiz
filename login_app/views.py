import flask

def render_login_app():
    return flask.render_template(template_name_or_list= 'login.html')
import flask

from flask_login import login_user, current_user

def loguot():
    flask.session.clear()
    return flask.redirect("/")

def render_home():
    return flask.render_template(
    template_name_or_list= 'home.html', 
    is_authorization = current_user.is_authenticated,
    username = current_user.name if current_user.is_authenticated else "", 
    is_teacher= current_user.is_teacher if current_user.is_authenticated else ""
    )



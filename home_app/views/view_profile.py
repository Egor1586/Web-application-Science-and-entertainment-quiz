import flask

from flask_login import current_user

def render_profile():
    
    return flask.render_template(
    template_name_or_list= 'profile.html', 
    is_authorization = current_user.is_authenticated,
    username = current_user.username if current_user.is_authenticated else "", 
    is_teacher= current_user.is_teacher if current_user.is_authenticated else ""
    )

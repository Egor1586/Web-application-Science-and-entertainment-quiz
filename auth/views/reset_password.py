import flask, Project

from .view_send_email import list_code
from .view_sing_up import user_data, list_code_account
from flask_login import current_user, login_user
from ..models import User

def render_reset_app():

    if flask.request.method == "POST":
        
        code = int(flask.request.form['code'])
        if code == list_code[-1]:
            return flask.redirect(location = '/../new_password')
        
    return flask.render_template('reset_password.html')


def render_confirm_account():
    if flask.request.method == "POST":
        code = int(flask.request.form['code'])
        if code == list_code_account[-1]:
                
            user = User(
                name = user_data['name'],
                email = user_data["email"],
                password = user_data['password'],
                password_confirmation = user_data['password_confirmation'],
                is_teacher = bool(user_data['is_teacher'])
            )                   
            
            Project.db.session.add(user)
            Project.db.session.commit()

            login_user(user)
            
            return flask.redirect(location = '/../')
    
    if not current_user.is_authenticated:
        return flask.render_template(template_name_or_list="reset_password.html")
    else:
        return flask.redirect('/')





import flask

from flask_login import login_user, current_user
from ..models import User


def render_login_app():
    if flask.request.method == "POST":
        password = flask.request.form["password"]
        email = flask.request.form["email"]
        
        list_users = User.query.all()

        for user in list_users:
            if user.email == email and user.password == password: 
                print("login")
                login_user(user)
                
    if not current_user.is_authenticated:
        return flask.render_template(template_name_or_list="login.html")
    else:
        return flask.redirect('/')

import flask_login, auth

from .settings import project

login_manager = flask_login.LoginManager(app= project)

@login_manager.user_loader
def load_user(id):
    return auth.User.query.get(id)

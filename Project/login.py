import flask_login, auth

from .settings import project

login_manager = flask_login.LoginManager(app= project)
login_manager.init_app(app= project)

login_manager.login_view = 'render_login_app'

@login_manager.user_loader
def load_user(id):
    return f'Id= {auth.User.query.get(id)}'
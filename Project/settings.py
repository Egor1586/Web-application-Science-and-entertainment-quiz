import flask, flask_sqlalchemy, flask_migrate, os, flask_login

import sign_up

project = flask.Flask(
    import_name = __name__,
    static_folder="static",
    static_url_path="/Project/",
    template_folder="templates",
    instance_path= os.path.abspath(os.path.join(__file__, '..', '..', 'instance'))
)

project.secret_key = "1234"

print(os.path.abspath(os.path.join(__file__, '..', 'instance')))


project.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = flask_sqlalchemy.SQLAlchemy(project)

migrate = flask_migrate.Migrate(app= project, db = db)

login_manager = flask_login.LoginManager(app= project)
login_manager.init_app(app= project)

login_manager.login_view = 'render_login_app'

@login_manager.user_loader
def load_user(id):
    return f'Id= {sign_up.User.query.get(id)}'


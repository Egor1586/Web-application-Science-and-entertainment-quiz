import flask, flask_sqlalchemy, flask_migrate, flask_login, random, dotenv, os, home_app, auth

from flask_mail import Mail

dotenv.load_dotenv()

project = flask.Flask(
    import_name = __name__,
    static_folder="static",
    static_url_path="/Project/",
    template_folder="templates",
    instance_path= os.path.abspath(os.path.join(__file__, '..', '..', 'instance'))
)

project.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='egor115819@gmail.com',
    MAIL_PASSWORD='zlvh btgp kbbj igyw',
)
mail = Mail(project)

project.secret_key = str(random.randint(10000, 99999))

print(os.path.abspath(os.path.join(__file__, '..', 'instance')))


project.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = flask_sqlalchemy.SQLAlchemy(project)

migrate = flask_migrate.Migrate(app= project, db = db)

login_manager = flask_login.LoginManager(app= project)
login_manager.init_app(app= project)

login_manager.login_view = 'render_login_app'

@login_manager.user_loader
def load_user(id):
    return f'Id= {auth.User.query.get(id)}'


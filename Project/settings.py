import flask, random, dotenv, os

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

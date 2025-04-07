import flask

from home_app import home_app
from score_app import score_app
from new_quiz_app import new_quiz_app
from profile_app import profile_app

project = flask.Flask(
    import_name = 'Project',
    static_url_path = '/static/',
    static_folder = 'static',
    template_folder = 'templates'
)

project.register_blueprint(blueprint = home_app)
project.register_blueprint(blueprint= score_app)
project.register_blueprint(blueprint= new_quiz_app)
project.register_blueprint(blueprint= profile_app)
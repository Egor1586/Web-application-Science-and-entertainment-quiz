import flask_sqlalchemy, flask_migrate 

from .settings import project

project.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = flask_sqlalchemy.SQLAlchemy(project)

migrate = flask_migrate.Migrate(app= project, db = db)
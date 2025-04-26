from .urls import *
from .settings import project, db
from .loadenv import load_env

# 
project.register_blueprint(blueprint = home_app)

# 
project.register_blueprint(blueprint = sign_up_app)

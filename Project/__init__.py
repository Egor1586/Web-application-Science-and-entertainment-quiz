from .urls import *
from .settings import project,socketio
from .loadenv import load_env
from .database import db
from .login import *
# 
project.register_blueprint(blueprint = home_app)

# 
project.register_blueprint(blueprint = sign_up_app)

# 
project.register_blueprint(blueprint= test_app)

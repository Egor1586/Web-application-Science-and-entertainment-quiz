from home_app import home_app, render_home
from score_app import score_app, render_score
from new_quiz_app import new_quiz_app, render_new_quiz
from profile_app import profile_app, render_profile_app
from login_app import login_app, render_login_app
from sign_up import sign_up_app, render_sign_up
from logout import logout_app, render_logout
from password_recovery import password_recovery_app, password_recovery

from .settings import project

home_app.add_url_rule(rule= "/", view_func= render_home)
score_app.add_url_rule(rule= '/score/', view_func= render_score, methods= ['GET', 'POST'])
new_quiz_app.add_url_rule(rule = '/new_quiz/', view_func = render_new_quiz, methods = ['GET', 'POST'])
profile_app.add_url_rule(rule="/profile/", view_func= render_profile_app, methods= ['GET', 'POST'])
login_app.add_url_rule(rule = '/login/', view_func = render_login_app, methods = ['GET', 'POST'])
sign_up_app.add_url_rule(rule="/sign_up/", view_func= render_sign_up, methods= ['GET', 'POST'])
logout_app.add_url_rule(rule="/logout/", view_func= render_logout, methods= ['GET', 'POST'])
password_recovery_app.add_url_rule(rule="/password_recovery/", view_func= password_recovery, methods= ['GET', 'POST'])



project.register_blueprint(blueprint = home_app)
project.register_blueprint(blueprint= score_app)
project.register_blueprint(blueprint= new_quiz_app)
project.register_blueprint(blueprint= profile_app)
project.register_blueprint(blueprint = login_app)
project.register_blueprint(blueprint = sign_up_app)
project.register_blueprint(blueprint = logout_app)
project.register_blueprint(blueprint = password_recovery_app)
from home_app import home_app, render_home
from score_app import score_app, render_score
from new_quiz_app import new_quiz_app, render_new_quiz
from profile_app import profile_app, render_profile_app
from login_app import login_app, render_login_app
from sign_up import sign_up_app, render_sign_up
from logout import logout_app, render_logout
from send_email import send_email_app, render_send_email
from confirmation import confirmation_app, render_confirmation
from reset_password_app import reset_password_app, render_reset_app
from new_password import new_password_app, render_new_password

from .settings import project

home_app.add_url_rule(rule= "/", view_func= render_home)
score_app.add_url_rule(rule= '/score/', view_func= render_score, methods= ['GET', 'POST'])
new_quiz_app.add_url_rule(rule = '/new_quiz/', view_func = render_new_quiz, methods = ['GET', 'POST'])
profile_app.add_url_rule(rule="/profile/", view_func= render_profile_app, methods= ['GET', 'POST'])
login_app.add_url_rule(rule = '/login/', view_func = render_login_app, methods = ['GET', 'POST'])
sign_up_app.add_url_rule(rule="/sign_up/", view_func= render_sign_up, methods= ['GET', 'POST'])
logout_app.add_url_rule(rule="/logout/", view_func= render_logout, methods= ['GET', 'POST'])
send_email_app.add_url_rule(rule="/send_email_app/", view_func= render_send_email, methods= ['GET', 'POST'])
confirmation_app.add_url_rule(rule="/confirmation/", view_func= render_confirmation, methods= ['GET', 'POST'])
reset_password_app.add_url_rule(rule= '/reset_password/', view_func= render_reset_app, methods= ['POST', 'GET'])
new_password_app.add_url_rule(rule= '/new_password/', view_func= render_new_password, methods= ['POST', 'GET'])



project.register_blueprint(blueprint = home_app)
project.register_blueprint(blueprint= score_app)
project.register_blueprint(blueprint= new_quiz_app)
project.register_blueprint(blueprint= profile_app)
project.register_blueprint(blueprint = login_app)
project.register_blueprint(blueprint = sign_up_app)
project.register_blueprint(blueprint = logout_app)
project.register_blueprint(blueprint = send_email_app)
project.register_blueprint(blueprint = confirmation_app)
project.register_blueprint(blueprint = reset_password_app)
project.register_blueprint(blueprint = new_password_app)
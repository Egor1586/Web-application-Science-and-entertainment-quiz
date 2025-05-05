from home_app import *
from home_app.views import *
from auth.app import *
from auth.views import *
from test_app import *


# 
home_app.add_url_rule(rule= "/", view_func= render_home)
home_app.add_url_rule(rule= '/score/', view_func= render_score, methods= ['GET', 'POST'])
home_app.add_url_rule(rule="/profile/", view_func= render_profile, methods= ['GET', 'POST'])
home_app.add_url_rule(rule = '/quizzes/', view_func = render_quizzes, methods = ['GET', 'POST'])


# 
sign_up_app.add_url_rule(rule="/sign_up/", view_func= render_sign_up, methods= ['GET', 'POST'])

sign_up_app.add_url_rule(rule="/send_email_app/", view_func= render_send_email, methods= ['GET', 'POST'])
sign_up_app.add_url_rule(rule= '/new_password/', view_func= render_new_password, methods= ['POST', 'GET'])
sign_up_app.add_url_rule(rule= '/reset_password/', view_func= render_reset_app, methods= ['POST', 'GET'])
sign_up_app.add_url_rule(rule= '/confirmation_account/', view_func= render_confirm_account, methods= ['POST', 'GET'])

sign_up_app.add_url_rule(rule = '/login/', view_func = render_login_app, methods = ['GET', 'POST'])

sign_up_app.add_url_rule(rule="/logout/", view_func= loguot, methods = ['GET', 'POST'])


# 
test_app.add_url_rule(rule= '/test_app/', view_func= render_test_app, methods = ['GET', 'POST'])
test_app.add_url_rule(rule= '/new_quiz/', view_func= render_new_quiz, methods = ['GET', 'POST'])
test_app.add_url_rule(rule= '/room/', view_func= render_room, methods = ['GET', 'POST'])
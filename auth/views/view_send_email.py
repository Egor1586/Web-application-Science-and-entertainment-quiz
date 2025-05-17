import flask
import random 

from Project.settings import project
from ..send_email import send_code

list_code = []
list_email = []
def render_send_email():

    if flask.request.method == 'POST':

        email = flask.request.form['email'] 
        code = random.randint(100000, 999999)
        list_code.append(code)
        list_email.append(email)

        with project.app_context():
            send_code(user_email= email, code= code)
        
        return flask.redirect(location = '/../reset_password')
    
    return flask.render_template(template_name_or_list= 'send_email.html')
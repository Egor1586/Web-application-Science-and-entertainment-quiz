import flask
import random 

from Project.settings import project
from .send_email import send_code

list_code = []

def render_send_email():

    if flask.request.method == 'POST':

        email = flask.request.form['email_input'] 
        print(f'Это email который мы получаем: {email}')
        code = random.randint(100000, 999999)
        list_code.append(code)

        with project.app_context():
            send_code(user_email= "egorgrockij1@gmail.com", code= code)
        
        return flask.redirect(location = '/../reset_password')
    
    return flask.render_template(template_name_or_list= 'send_email.html')
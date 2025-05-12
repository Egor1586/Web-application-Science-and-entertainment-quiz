import flask, traceback, random
import Project

from ..models import User
from flask_login import current_user
from ..send_email import send_code

user_data = {
    "name": None,
    'password': None,
    'password_confirmation': None,
    'email': None,
    'is_teacher': None
    }


list_code_account = []

def render_sign_up(): 
    message= ''
   
    if flask.request.method == 'POST':
        try:   
            user_data["name"] = flask.request.form['name'] 
            user_data["password"]= flask.request.form['password'] 
            user_data["password_confirmation"]= flask.request.form['password-confirmation']
            user_data["email"]= flask.request.form['email']
            role = flask.request.form['is_teacher']
            if role == "False":
                user_data['is_teacher'] = False
            else:
                user_data['is_teacher'] = True
       
            code= random.randint(100000, 999999)
            list_code_account.append(code)

            db_email = User.query.filter_by(email = user_data["email"]).first()
            
            if user_data["password"] == user_data["password_confirmation"]: 
                if db_email is None:

                    with Project.project.app_context():
                        send_code(user_email=user_data["email"], code= code)

                    return flask.redirect(location = '/confirmation_account')

            else:
                print('Not same password')

                
        except Exception as e:
            print(e)
            traceback.print_exc()
    

    return flask.render_template(template_name_or_list= 'sign_up.html', message= message)
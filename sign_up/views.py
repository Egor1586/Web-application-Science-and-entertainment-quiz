import flask, os
from .models import User
from Project.settings import db

def render_sign_up():
    is_registrated = False 
    teacher = False
    
    if flask.request.method == 'POST':
        try:
            password = flask.request.form['password'] 
            password_confirmation = flask.request.form['password-confirmation']
            
            if password == password_confirmation: 
                print(f'одинаковые пароли')
                if flask.request.form['is_teacher'] == 'True':
                    teacher = True

                    
                user = User(
                    name = flask.request.form['name'],
                    email = flask.request.form['email'],
                    password = password,
                    password_confirmation = password_confirmation,
                    is_teacher = teacher
                )

                data = db.session.add(user)
                db.session.commit()
                return flask.redirect('/../', code = 301)

            else:
                print('Not same password')

                
        except Exception as e:
            print(e)
    
    
    
    
    return flask.render_template(template_name_or_list= 'sign_up.html')
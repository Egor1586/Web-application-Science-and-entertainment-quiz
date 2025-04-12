import flask, os
from .models import User
from Project.settings import db

def render_sign_up():
    is_registrated = False 
    
    if flask.request.method == 'POST':
        try:
            user = User(
                name = flask.request.form['name'],
                email = flask.request.form['email'],
                password = flask.request.form['password'],
                password_confirmation = flask.request.form['password-confirmation'],
                # is_teacher = flask.request.form['is_teacher']
            )
            
            if user.password == user.password_confirmation:
        
                db.session.add(user)
                db.session.commit()
                
                is_registrated = True
            else:
                print('Different passwords')
                
        except Exception as e:
            print(e)
    
    
    
    
    return flask.render_template(template_name_or_list= 'sign_up.html', context= [])


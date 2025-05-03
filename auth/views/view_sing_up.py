import flask, traceback
import Project

from ..models import User
from ..confirmation import confirmation_email

def render_sign_up(): 
    teacher = False
    message= ''

    # with Project.project.app_context():
    #     confirmation_email("egorgrockij1@gmail.com")

    if flask.request.method == 'POST':
        try:
            password = flask.request.form['password'] 
            password_confirmation = flask.request.form['password-confirmation']
            email = flask.request.form['email']
            
            if password == password_confirmation: 
                print(f'одинаковые пароли')
                if flask.request.form['is_teacher'] == 'True':
                    teacher = True
                    
                user = User(
                    name = flask.request.form['name'],
                    email = email,
                    password = password,
                    password_confirmation = password_confirmation,
                    is_teacher = teacher,
                    is_certified = False
                )
                
                flask.session['username'] = user.name
                flask.session['is_teacher'] = user.is_teacher

                Project.db.session.add(user)
                Project.db.session.commit()

                flask.session['is_registrated'] = True
                
                with Project.project.app_context():
                    confirmation_email(email)

                message = "Confirm your account by email"

                # return flask.redirect('/../', code = 301)

            else:
                print('Not same password')

                
        except Exception as e:
            print(e)
            traceback.print_exc()
    

    return flask.render_template(template_name_or_list= 'sign_up.html', message= message)
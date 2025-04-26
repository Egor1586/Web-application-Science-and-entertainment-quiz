import flask

from flask_login import login_user
from ..models import User


def render_login_app():
    if flask.request.method == 'POST':
        try:
            user_password = flask.request.form['password']
                    
            for user in User.query.filter_by(email = flask.request.form['email']):
                if user.password == user_password:
                    login_user(user)

                    flask.session['username'] = user.name

                    flask.session['is_registrated'] = True

                    return flask.redirect('/../')             
                    
        except Exception as error:
            print(f'An error: {error}') 

    # user.is_authenticated:

    return flask.render_template(template_name_or_list= 'login.html', content= [])
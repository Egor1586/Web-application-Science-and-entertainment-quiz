import flask
import sign_up

from flask_login import login_user, current_user


def render_login_app():
    if flask.request.method == 'POST':
        try:
            user_name = flask.request.form['name']
            user_password = flask.request.form['password']
                    
            for user in sign_up.User.query.filter_by(name = flask.request.form['name']):
                if user.password == user_password:
                    login_user(user)

                    flask.session['is_registrated'] = True

                    return flask.redirect('/../')             
                    
        except Exception as error:
            print(f'An error: {error}') 

    # if not current_user.is_authenticated:
    #     print(f'Это дата которую мы возвращаем: {flask.render_template(template_name_or_list= 'login.html', content= [])}')
    return flask.render_template(template_name_or_list= 'login.html', content= [])
                

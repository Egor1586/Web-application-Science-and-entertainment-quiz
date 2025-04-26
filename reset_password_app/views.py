import flask

from send_email.views import list_code, list_email
from sign_up.models import User
from Project.settings import db

def render_reset_app():

    if flask.request.method == "POST":
        code = int(flask.request.form['code'])
        print(f'Это список email: {list_email[0]}')
        user = User.query.filter_by(email = list_email[0]).first()
        print(f'Это юзер которого мы получили')
        if user:
            user.password = 'Тут какой-то пароль'
            db.session.commit()
        elif code == list_code[-1]:
            print('Все хорошо')
            return flask.redirect(location = '/../new_password')
        
    return flask.render_template('reset_password.html')

import flask
import Project

from flask_login import logout_user
from ..models import User


def render_confirmation():
    flags = ['is_registrated']
    context = {flag: flask.session.get(flag, False) for flag in flags}

    user_email = flask.request.args.get('user_email')
    print(user_email)

    if flask.request.method == 'POST':
        try:
            in_account = bool(flask.request.form.get('submit'))  
            print(in_account, type(in_account))

            for user in User.query.filter_by(email = user_email):
                if user.email == user_email:
                    user.is_certified = True

                    Project.db.session.commit()

                    return flask.redirect('/../')         

        except Exception as e:
            print(e)

    return flask.render_template('confirmation.html', user_email=user_email, **context)


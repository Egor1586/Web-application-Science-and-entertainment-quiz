import flask
import sign_up

from Project.settings import db

def render_confirmation():
    flags = ['is_registrated']
    context = {flag: flask.session.get(flag, False) for flag in flags}

    user_email = flask.request.args.get('user_email')
    print(user_email)

    if flask.request.method == 'POST':
        try:
            in_account = bool(flask.request.form.get('submit'))  
            print(in_account, type(in_account))

            for user in sign_up.User.query.filter_by(email = user_email):
                if user.email == user_email:
                    user.in_account = True

                    db.session.commit()

                    return flask.redirect('/../')         

        except Exception as e:
            print(e)

    return flask.render_template('confirmation.html', user_email=user_email, **context)
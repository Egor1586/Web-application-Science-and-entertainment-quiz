import flask

from .view_send_email import list_code

def render_reset_app():

    if flask.request.method == "POST":
        code = int(flask.request.form['code'])
        if code == list_code[-1]:
            print('Все хорошо')
            return flask.redirect(location = '/../new_password')
        
    return flask.render_template('reset_password.html')

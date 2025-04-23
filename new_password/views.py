import flask
from sign_up.models import User

def render_new_password():
    if flask.request.method == "POST":
        new_password = flask.request.form['new_pas']
        conf_password = flask.request.form['new_pas_conf']

        if new_password == conf_password:
            pass
    
    return flask.render_template('new_password.html')
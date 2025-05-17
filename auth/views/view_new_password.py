import flask, Project
from .view_send_email import list_email
from ..models import User



def render_new_password():
    
    if flask.request.method == "POST":
        new_password = flask.request.form['new_pas']
        conf_password = flask.request.form['new_pas_conf']

        for user in User.query.filter_by(email = list_email[0]):
            if user and new_password == conf_password:
                user.password = str(new_password)
                user.password_confirmation = str(new_password)
                Project.db.session.commit()
                
                return flask.redirect(location = '/../login')
    
    return flask.render_template('new_password.html')
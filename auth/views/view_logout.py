import flask

from flask_login import logout_user

def render_logout():
    if flask.request.method == 'POST':
        logout_user()
        
        flask.session['is_registrated'] = False
        
        return flask.redirect(location = '/')
    
    return flask.render_template(template_name_or_list = 'logout.html')


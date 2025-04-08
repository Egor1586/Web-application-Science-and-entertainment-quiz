import flask 

def render_sign_up():
    return flask.render_template(template_name_or_list= 'sign_up.html')


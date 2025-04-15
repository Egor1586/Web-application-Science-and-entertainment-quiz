import flask

def render_home():

    flags = ['is_registrated']
    context = {flag: flask.session.get(flag, False) for flag in flags}

    return flask.render_template(template_name_or_list= 'home.html', **context)
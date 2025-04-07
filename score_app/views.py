import flask

def render_score():
    return flask.render_template(template_name_or_list= 'score.html')
import flask

def render_edit_question():

    return flask.render_template(
        template_name_or_list = 'edit_question.html'
    )
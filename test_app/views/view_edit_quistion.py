import flask

from flask_login import current_user

def render_edit_question():

    return flask.render_template(
        template_name_or_list = 'edit_question.html',
        is_authorization = current_user.is_authenticated,
        username = current_user.username if current_user.is_authenticated else "", 
        is_teacher= current_user.is_teacher if current_user.is_authenticated else ""
    )
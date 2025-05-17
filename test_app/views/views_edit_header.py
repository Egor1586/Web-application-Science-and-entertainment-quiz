import flask
from ..models import Test, Quiz

from Project.database import db

from flask_login import current_user

def render_edit_header():

    return flask.render_template(
        template_name_or_list = 'edit_head_test.html'
    )
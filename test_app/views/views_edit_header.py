import flask
from ..models import Test, Quiz

from Project.database import db

from flask_login import current_user

def render_edit_header(id):

    test= Test.query.filter_by(id= id).first()

    if flask.request.method == "POST":

        topic = flask.request.form["topic"]
        description = flask.request.form["description"]

        test.topic = topic
        test.description = description

        db.session.commit()

    return flask.render_template(
        template_name_or_list = 'edit_head_test.html',
        is_authorization = current_user.is_authenticated,
        username = current_user.username if current_user.is_authenticated else "", 
        is_teacher= current_user.is_teacher if current_user.is_authenticated else ""
    )
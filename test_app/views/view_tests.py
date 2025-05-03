import flask
from test_app.models import Test
def render_test_app():
    is_registrated = flask.session.get('is_registrated', False)
    username = flask.session.get('username')

    test_id = flask.request.args.get('test_id')
    print(test_id)

    for test in Test.query.filter_by(id = test_id):
        print(test)
        topic = test.topic

    return flask.render_template("test.html", is_registrated=is_registrated, username=username, is_teacher= flask.session.get("is_teacher"), topic= topic)
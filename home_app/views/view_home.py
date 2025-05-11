import flask

from flask_login import login_user, current_user
from Project.settings import socketio
from flask_socketio import emit, join_room
from test_app.models import Test

@socketio.on('join')
def handle_join(data):
    room = data['room']
    username = data['username']
    join_room(room)
    emit('user_joined', {'msg': f'{username} присоединился к комнате {room}'}, room=room)

def loguot():
    flask.session.clear()
    return flask.redirect("/")

def render_home():
    list_test = []
    if current_user.is_authenticated:
        list_test = Test.query.all()

    return flask.render_template(
    template_name_or_list= 'home.html', 
    is_authorization = current_user.is_authenticated,
    username = current_user.username if current_user.is_authenticated else "", 
    is_teacher= current_user.is_teacher if current_user.is_authenticated else "",
    list_tests = list_test
    )
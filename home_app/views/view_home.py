import flask, Project

from flask_login import login_user, current_user
from Project.settings import socketio
from flask_socketio import emit, join_room
from test_app.models import Test


users = {}

@Project.settings.socketio.on('join')
def handle_join(username):
    username = username
    users[flask.request.sid] = username
    join_room(username)
    emit('user_joined', {'msg': f'{username} присоединился к комнате {username}'}, room= username)
    print(f'{username} присоединился к комнате {username}')

@Project.settings.socketio.on('message')
def handle_message(data):
    username = users.get(flask.request.sid, "Anonymous")  # Get the user's name
    emit("message", f"{username}: {data}", broadcast=True)  # Send to everyone
    print(f"{username}: {data}")

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
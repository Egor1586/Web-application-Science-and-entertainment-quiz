import flask, Project

from flask_login import current_user
from flask_socketio import join_room, emit

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

def render_room(code):
    
    return flask.render_template(
    template_name_or_list= 'room.html', 
    is_authorization = current_user.is_authenticated,
    username = current_user.username if current_user.is_authenticated else "", 
    is_teacher= current_user.is_teacher if current_user.is_authenticated else "",
    CODE = code
    )
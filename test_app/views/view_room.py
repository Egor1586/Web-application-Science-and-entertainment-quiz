import flask, Project

from flask_login import current_user
from flask_socketio import join_room, emit

@Project.settings.socketio.on('join')
def handle_join(data):
    room = data['room']
    username = data['username']
    join_room(room)
    emit('user_joined', {'msg': f'{username} присоединился к комнате {room}'}, room=room)

def render_room():
    CODE = 1111
    
    return flask.render_template(
    template_name_or_list= 'room.html', 
    is_authorization = current_user.is_authenticated,
    username = current_user.username if current_user.is_authenticated else "", 
    is_teacher= current_user.is_teacher if current_user.is_authenticated else "",
    CODE= CODE
    )
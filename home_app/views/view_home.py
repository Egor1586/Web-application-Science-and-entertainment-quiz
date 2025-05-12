import flask

from flask_login import current_user
from Project.settings import socketio, sock
from flask_socketio import emit, join_room
from test_app.models import Test


@socketio.on('join')
def handle_join(data):
    room = data['room']
    username = data['username']
    join_room(room)
    emit('user_joined', {'msg': f'{username} присоединился к комнате {room}'}, room=room)

#=========================================================================================
@sock.route('/ws/<room>')
def handle_join(ws, room, data):
    while True:
        try:
            room = data['room']
            data = ws.recieve()
            if data is None:
                break
            for client in room:
                if client != ws:
                    try:
                        client.send(data)
                    except:
                        pass
        except Exception as error:
            print(f'An error: {error}')

        finally:
            room.remove(ws)
            if not room:
                del room
#=========================================================================================

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
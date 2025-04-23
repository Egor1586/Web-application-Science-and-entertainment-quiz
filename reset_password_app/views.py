import flask

from send_email.views import list_code

def render_reset_app():

    if flask.request.method == "POST":
        code = int(flask.request.form['code'])
        print(list_code)
        print(code)
        print(type(list_code[0]))
        print(type(code))
        if code == list_code[-1]:
            print('Все хорошо')
            return flask.redirect(location = '/../new_password')
        
    return flask.render_template('reset_password.html')

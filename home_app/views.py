import flask

# flags = ['is_registrated']
# context = {flag: flask.session.get(flag, False) for flag in flags}
# name = flask.session.get('name')

def render_home():
    is_registrated = flask.session.get('is_registrated', False)
    username = flask.session.get('username')

    print(flask.session.get("is_teacher"))
    return flask.render_template(template_name_or_list= 'home.html', is_registrated=is_registrated, username=username, is_teacher= flask.session.get("is_teacher"), )


def render_score():
    is_registrated = flask.session.get('is_registrated', False)
    username = flask.session.get('username')
    
    return flask.render_template(template_name_or_list= 'score.html', is_registrated=is_registrated, username=username, is_teacher= flask.session.get("is_teacher"))


def render_profile():
    is_registrated = flask.session.get('is_registrated', False)
    username = flask.session.get('username')

    return flask.render_template(template_name_or_list= 'profile.html', is_registrated=is_registrated, username=username, is_teacher= flask.session.get("is_teacher"))


def render_new_quiz():
    is_registrated = flask.session.get('is_registrated', False)
    username = flask.session.get('username')
    
    if flask.request.method == "POST":
        try:
            topic = flask.request.form['topic']
            count_question = flask.request.form['count_question']
            answer_on_question = flask.request.form["answer_on_question"]
            if not count_question:
                count_question = 10
            if not answer_on_question:
                answer_on_question = 4

            print(topic,count_question,answer_on_question)
        except:
            pass



    return flask.render_template(template_name_or_list = 'new_quiz.html', is_registrated=is_registrated, username=username, is_teacher= flask.session.get("is_teacher"))

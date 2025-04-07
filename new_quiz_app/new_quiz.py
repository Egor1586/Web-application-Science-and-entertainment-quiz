import flask 

new_quiz_app = flask.Blueprint(
    name = 'new_quiz_app',
    import_name = __name__,
    static_folder = 'static',
    static_url_path = '/new_quiz_app/',
    template_folder = 'templates'
)

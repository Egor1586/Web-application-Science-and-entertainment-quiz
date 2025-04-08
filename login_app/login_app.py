import flask

login_app = flask.Blueprint(
    name = 'login_app',
    import_name = __name__,
    static_folder= 'static',
    static_url_path= '/login_app/',
    template_folder= 'templates'
)
import flask

logout_app = flask.Blueprint(
    name = 'logout_app',
    import_name= __name__,
    template_folder= 'templates',
    static_url_path= '/logout/'
)
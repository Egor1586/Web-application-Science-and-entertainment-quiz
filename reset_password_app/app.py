import flask 

reset_password_app = flask.Blueprint(
    name= 'reset_password_app',
    template_folder= 'templates',
    import_name= __name__,
    static_folder= 'static',
    static_url_path= '/reset_password/'
)
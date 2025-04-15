import flask 

password_recovery_app = flask.Blueprint(
    name= 'password_recovery_app',
    import_name= __name__,
    static_folder= 'static',
    template_folder= 'templates',
    static_url_path= '/password_recovery/'
)
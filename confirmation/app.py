import flask 

confirmation_app = flask.Blueprint(
    name= 'confirmation_app',
    import_name= __name__,
    static_folder= 'static',
    static_url_path= '/confirmation_app/',
    template_folder= 'templates'
)
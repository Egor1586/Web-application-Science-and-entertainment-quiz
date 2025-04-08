import flask 

home_app = flask.Blueprint(
    name= 'home_app',
    import_name= __name__,
    static_folder= 'static',
    static_url_path= '/home_app/',
    template_folder= 'templates'
)
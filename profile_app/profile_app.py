import flask 

profile_app = flask.Blueprint(
    name = 'profile_app',
    import_name = __name__,
    static_folder= 'static',
    static_url_path= '/profile_app/',
    template_folder= 'templates'
)
import flask 

new_password_app = flask.Blueprint(
    name= 'new_password',
    template_folder= 'templates',
    import_name= __name__,
    static_folder= 'static',
    static_url_path= '/new_password/'
)
import flask 

sign_up_app = flask.Blueprint(
    name= 'sign_up',
    import_name= __name__,
    static_folder= 'static',
    template_folder= 'templates',
    static_url_path= '/sign_up/'
)
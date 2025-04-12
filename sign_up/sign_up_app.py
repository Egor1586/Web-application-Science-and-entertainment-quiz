import flask 

sign_up_app = flask.Blueprint(
    name= 'sign_up_app',
    import_name= 'sign_up',
    static_folder= 'static',
    template_folder= 'templates',
    static_url_path= '/sign_up/'
)

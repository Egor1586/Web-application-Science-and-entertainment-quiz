import flask

score_app = flask.Blueprint(
    name = 'score_app', 
    import_name= __name__,
    static_url_path= '/score_app/',
    template_folder= 'templates',
    static_folder= 'static'
)
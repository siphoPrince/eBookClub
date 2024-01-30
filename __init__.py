from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRETE_KEY'] = 'eBook'


    from eBookClub.views.app_views import app_views
    from .auth import login

    app.register_blueprint(app_views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
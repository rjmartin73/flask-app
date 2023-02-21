from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'N4gU7oMzyYc93fnnpHz4DRCivWYnC3ZKP6GDRbrjU7wUC7GfWoGDeaFknQ9pB3nd'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

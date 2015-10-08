from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from views import bp

db = SQLAlchemy()

from views import index

def create_app():
    app = Flask(__name__)

    app.register_blueprint(bp)

    db.init_app(app)

    @app.route('/favicon.ico')
    def favicon():
        return ''

    return app
from flask import Flask

from .extension import db
from .view import bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)

    connection_string: str = (f'root:root@localhost:3306')
    app.config[
        'SQLALCHEMY_DATABASE_URI'
    ] = f'mysql+pymysql://{connection_string}/user'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    return app

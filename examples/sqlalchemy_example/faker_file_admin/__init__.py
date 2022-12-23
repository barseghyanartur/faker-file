import os
import os.path as op

from flask import Flask, request, session
from flask_babelex import Babel
from flask_sqlalchemy import SQLAlchemy

from .data import build_sample_db

app: Flask
db: SQLAlchemy


def create_app(config_filename: str) -> Flask:
    global app
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    global db
    db = SQLAlchemy(app)

    with app.app_context():
        # Build a sample db on the fly, if one does not exist yet.
        app_dir = op.join(
            op.realpath(os.path.dirname(__file__)), "faker_file_admin"
        )
        database_path = op.join(app_dir, app.config["DATABASE_FILE"])
        if not os.path.exists(database_path):
            build_sample_db(db)

    return app


create_app("config.py")


# Initialize babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    override = request.args.get("lang")

    if override:
        session["lang"] = override

    return session.get("lang", "en")


import faker_file_admin.main  # noqa

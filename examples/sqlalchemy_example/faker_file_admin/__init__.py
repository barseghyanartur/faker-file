from flask import Flask, request, session
from flask_babelex import Babel
from flask_sqlalchemy import SQLAlchemy

app: Flask
db: SQLAlchemy

# app = Flask(__name__)
# app.config.from_pyfile('config.py')
# db = SQLAlchemy(app)


def create_app(config_filename: str) -> Flask:
    global app
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    global db
    db = SQLAlchemy(app)

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


import faker_file_admin.main

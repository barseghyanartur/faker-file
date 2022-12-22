import flask_admin as admin
from flask import send_file
from flask_admin.contrib import sqla

from . import app, db
from .models import Upload


# Flask views
@app.route("/")
def index():
    tmp = """
<p><a href="/admin/?lang=en">Click me to get to Admin! (English)</a></p>
<p><a href="/admin/?lang=cs">Click me to get to Admin! (Czech)</a></p>
<p><a href="/admin/?lang=de">Click me to get to Admin! (German)</a></p>
<p><a href="/admin/?lang=es">Click me to get to Admin! (Spanish)</a></p>
<p><a href="/admin/?lang=fa">Click me to get to Admin! (Farsi)</a></p>
<p><a href="/admin/?lang=fr">Click me to get to Admin! (French)</a></p>
<p><a href="/admin/?lang=pt">Click me to get to Admin! (Portuguese)</a></p>
<p><a href="/admin/?lang=ru">Click me to get to Admin! (Russian)</a></p>
<p><a href="/admin/?lang=pa">Click me to get to Admin! (Punjabi)</a></p>
<p><a href="/admin/?lang=zh_CN">
Click me to get to Admin! (Chinese - Simplified)</a></p>
<p><a href="/admin/?lang=zh_TW">
Click me to get to Admin! (Chinese - Traditional)</a></p>
"""
    return tmp


@app.route("/favicon.ico")
def favicon():
    return send_file("static/favicon.ico")


# Create admin
admin = admin.Admin(app, name="Example: SQLAlchemy", template_mode="bootstrap4")

# Add views
admin.add_view(sqla.ModelView(Upload, db.session))

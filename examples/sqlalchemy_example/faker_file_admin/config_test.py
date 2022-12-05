# set optional bootswatch theme
# see http://bootswatch.com/3/ for available swatches
FLASK_ADMIN_SWATCH = "cerulean"

# Create dummy secrey key so we can use sessions
SECRET_KEY = "123456790"

# Create in-memory database
DATABASE_FILE = "sample_db_test.sqlite"
SQLALCHEMY_DATABASE_URI = "sqlite://"
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from solarvibes.config import Config


app = Flask(__name__)                               # creates the flask app
app.config.from_object(Config)                   # imports app configuration from config.py


db = SQLAlchemy(app)                                # create database connection object

#############################
# Begin Import Models
#############################
# from solarvibes.site.models import
#############################
# End Import Models
#############################



#############################
# Begin Import Views
#############################
from solarvibes import views
from solarvibes.site.views import site

app.register_blueprint(site, url_prefix='/web')
#############################
# End Import Views
#############################

from flask_sqlalchemy import SQLAlchemy
from .common.config import Config

from flask import Flask
from flask_restful import Api
import sys
sys.path.append("..")

# all major dependencies are defiend here itself maintaining modularity

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
db = SQLAlchemy(app)

#  avoiding circular imports
from .resources.routes import initialize_routes
initialize_routes(api)

from .common.models import Record

db.create_all()


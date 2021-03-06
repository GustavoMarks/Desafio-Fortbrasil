from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_marshmallow import Marshmallow
from flask_login import LoginManager

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config.from_object("config")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

ma = Marshmallow(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(app)

from app.models import tables
from app.controllers import default
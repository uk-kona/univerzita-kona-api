from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .api import PaymentResource
from .config import Config

api = Blueprint('api', __name__)
api.add_url_rule('/payment/', view_func=PaymentResource.as_view('payment'))

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api, url_prefix='/api/v1')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

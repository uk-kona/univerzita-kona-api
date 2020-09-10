from flask import Flask, Blueprint
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .api import PaymentResource, WantToHelpResource, NeedHelpResource
from .config import Config

api = Blueprint('api', __name__)
api.add_url_rule('/payment', view_func=PaymentResource.as_view('payment'))
api.add_url_rule('/want-to-help', view_func=WantToHelpResource.as_view('want-to-help'))
api.add_url_rule('/need-help', view_func=NeedHelpResource.as_view('need-help'))

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
app.register_blueprint(api, url_prefix='/api/v1')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .api import PaymentResource
api = Blueprint('api', __name__)
api.add_url_rule('/payment/', view_func=PaymentResource.as_view('payment'))
app.register_blueprint(api, url_prefix='/api/v1')

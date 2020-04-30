from flask import Flask, Blueprint

from .api import PaymentResource

api = Blueprint('api', __name__)
api.add_url_rule('/payment/', view_func=PaymentResource.as_view('payment'))

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api/v1')

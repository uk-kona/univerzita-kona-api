from flask import jsonify
from flask.views import MethodView


class PaymentResource(MethodView):
    def get(self):
        return jsonify(ok=True)

    def post(self):
        pass

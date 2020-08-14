from flask import jsonify
from flask.views import MethodView


class PaymentResource(MethodView):
    def get(self):
        return jsonify(ok=True)

    def post(self):
        pass


class WantToHelpResource(MethodView):
    def post(self):
        return jsonify(ok=True)


class NeedHelpResource(MethodView):
    def post(self):
        return jsonify(ok=True)

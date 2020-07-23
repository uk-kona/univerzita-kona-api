from app import db
from flask import jsonify, request
from .models import Payment
from flask.views import MethodView
from http import HTTPStatus


class PaymentResource(MethodView):
    def post(self):
        content = request.json
        if content is None:
            return jsonify(error='No JSON provided when calling PAYMENT/POST API'), HTTPStatus.BAD_REQUEST
        if 'note' not in content:
            return jsonify(error='Wrong JSON provided when calling PAYMENT/POST API, note not provided'), \
                   HTTPStatus.BAD_REQUEST
        p = Payment(note=content['note'])
        db.session.add(p)
        db.session.commit()
        return jsonify({"variable_symbol": p.variable_symbol})

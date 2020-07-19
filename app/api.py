from app import db
from flask import jsonify
from flask import request
from .models import Payment
from flask.views import MethodView


class PaymentResource(MethodView):
    def post(self):
        content = request.json
        if 'note' not in content:
            raise KeyError
        highest_id = db.session.query(db.func.max(Payment.id)).scalar()
        if highest_id is None:
            highest_id = 0
        leading_zeros = ('0' * (10 - len(str(highest_id + 1))))
        new_variable_symbol = leading_zeros + str(highest_id + 1)
        p = Payment(variable_symbol=new_variable_symbol, note=content['note'])
        db.session.add(p)
        db.session.commit()
        return jsonify({"variable_symbol": new_variable_symbol})

from . import db


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.relationship('PaymentData(db.Model)', backref='payment', lazy='dynamic')


class PaymentData(db.Model):
    note = db.Column(db.String(300))
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.id'))

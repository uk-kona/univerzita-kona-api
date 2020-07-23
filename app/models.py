from app import db


class Payment(db.Model):
    variable_symbol = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(256))

    def __repr__(self):
        return f'<Payment: [VS: {self.variable_symbol}, note: {self.note}]>'

from app import db


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    variable_symbol = db.Column(db.String(10), unique=True)
    note = db.Column(db.String(256))

    def __repr__(self):
        return '<Payment: [id: {}, VS: {}, note: {}]>'.format(self.id, self.variable_symbol, self.note)

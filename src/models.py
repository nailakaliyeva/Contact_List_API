from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    full_name = db.Column(db.String(50), unique=True, nullable=False)

    # def __repr__(self):
    #     return '<Person %r>' % self.full_name

    def serialize(self):
        return {
            "address": self.address,
            "email": self.email,
            "phone": self.phone,
            "full_name": self.full_name,
            "id": self.id
        }
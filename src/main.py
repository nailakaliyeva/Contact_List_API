"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/hello', methods=['POST', 'GET'])
def handle_person():

    response_body = {
        "hello": "world"
    }

    return jsonify(response_body), 200

@app.route("/contact", methods=['POST', 'GET'])
def handle_contact():
    if  request.method == "POST":
        body = request.get_json()

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if 'full_name' not in body:
            raise APIException('You need to specify the full name', status_code=400)
        if 'email' not in body:
            raise APIException('You need to specify the email', status_code=400)
        contact1 = Person(full_name=body['full_name'], email=body['email'], address=body["address"], phone=body["phone"])
        db.session.add(contact1)
        db.session.commit()
        return "ok", 200
    # GET request
    if request.method == 'GET':
        all_people = Person.query.all()
        all_people = list(map(lambda x: x.serialize(), all_people))
        return jsonify(all_people), 200
    return "Invalid Method", 404

@app.route("/update/<int:person_id>", methods=["PUT", "DELETE"])
def update_contact(person_id):
    if request.method == "PUT":
        body = request.get_json()
        contact1 = Person.query.get(person_id)
        print(person_id)
        if "address" in body:
            contact1.address = body["address"]
        if "phone" in body:
            contact1.phone = body["phone"]
        if "email" in body:
            contact1.email = body["email"]
        if "full_name" in body:
            contact1.full_name = body["full_name"]
            db.session.commit()
            return jsonify(contact1.serialize()), 200
    if request.method == "DELETE":
        contact1 = Person.query.get(person_id)
        db.session.delete(contact1)
        db.session.commit()
        return "ok", 200


















# this only runs if `$ python src/main.py` is exercuted
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)

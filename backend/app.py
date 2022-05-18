# app.py
from bson.json_util import dumps, loads
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)
CORS(app)
# Stringa di connessione al DB
#app.config["MONGO_URI"] = os.getenv('MONGO_URI')

#mongo = PyMongo(app)
# Per rispondere alle chiamate cross origin

# Annotation that allows the function to be hit at the specific URL.
print(os.getenv('GITPOD_WORKSPACE_URL'))


@app.route("/")
# Generic Python functino that returns "Hello world!"
def index():
    return "Hello world!"


@app.route('/api/user/<id>', methods=['GET'])
def get_user_data(id):
    data = {
        'id': id,
        'name': 'Ugo',
        'surname': 'Foo'
    }
    return jsonify(data)


# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(host='0.0.0.0')

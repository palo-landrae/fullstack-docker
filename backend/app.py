# app.py
from dotenv import load_dotenv
import os
load_dotenv()

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps, loads

app = Flask(__name__)

# Stringa di connessione al DB
#app.config["MONGO_URI"] = os.getenv('MONGO_URI')

#mongo = PyMongo(app)
# Per rispondere alle chiamate cross origin

# Annotation that allows the function to be hit at the specific URL.
@app.route("/")
# Generic Python functino that returns "Hello world!"
def index():
    return "Hello world!"

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(host='0.0.0.0')

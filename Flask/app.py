from flask import Flask, render_template, session, request, redirect, url_for
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/add_data": {"origins": "https://repl.it"}})
app.config['CORS_HEADERS'] = 'Content-Type'
#app.config['MONGO_URI'] = os.getenv('MONGO_URI')
#mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_data', methods=["POST"])
@cross_origin()
def add_data():
    print(request.form.get("name"))
    print(request.form.get("url"))
    return "Added info to database"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
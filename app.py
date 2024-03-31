from flask import Flask, request, flash, url_for, redirect, render_template
from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from flask import jsonify
import json
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
load_dotenv()

app = Flask(__name__)
CORS(app)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")

db = SQLAlchemy(app)
migrate = Migrate(app,db)

_API_PREFIX = "/api/"
from routes.patients import patients_blueprint
from routes.doctors import doctors_blueprint
from routes.departments import department_blueprint


def create_app():
    db.init_app(app)
    db.create_all()
    app.register_blueprint(patients_blueprint, url_prefix=f"{_API_PREFIX}/patient")
    app.register_blueprint(doctors_blueprint, url_prefix=f"{_API_PREFIX}/doctor")
    app.register_blueprint(department_blueprint, url_prefix=f"{_API_PREFIX}/department")
    return app



# Configure Swagger UI
SWAGGER_URL = '/swagger'
SWAGGER_JSON_FILE_PATH = os.getenv("SWAGGER_JSON_FILE_PATH")
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    SWAGGER_JSON_FILE_PATH,
    config={
        'app_name': "Hospital Management Solution"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def swagger():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))

#!/usr/bin/env python3
"""Flask Application"""

from flask import Flask, make_response, jsonify
from api.v1.views import app_views
from flask_cors import CORS
from models import storage
import os
from werkzeug.utils import secure_filename

projectDirectory = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(projectDirectory, 'attachments')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def fourOfFour(err):
    """Returns 404 error"""
    return make_response(jsonify({'Error': 'Resource Not Found'}), 404)


@app.teardown_appcontext
def tearDown(self):
    """Removes the current database session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000, threaded=True)

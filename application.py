from flask import Flask, jsonify
from flask_cors import CORS
from database.db import *

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

# Import and register the user blueprint
from database.routes.users import users_bp
app.register_blueprint(users_bp, url_prefix='/api')

@app.route('/', methods=['GET'])
def home():
    return jsonify("homepage")

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('FLASK server running!')

if __name__ == '__main__':
    app.run()

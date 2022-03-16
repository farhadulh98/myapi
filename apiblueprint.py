import flask
import home
import contact

from flask import Flask, jsonify
from home import home_bp
from contact import contact_bp
app = Flask(__name__)
app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(contact_bp, url_prefix='/contact')

@app.route('/', methods=['GET'])
def ranapp():
    return "Basic page"
app.run(debug=True)
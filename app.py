from flask import Flask
from flask import Flask, request, send_from_directory
from grammar import *
from app import app
import json

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

#app = Flask(__name__)

@app.route('/<path:path')
def initiate():
    #return send_from_directory('index.htm', path)
    return send_from_directory(app.config['index.html'], index.html, as_attachment=True)


@app.route('/<path:equation>')
def index(equation):
    return json.dumps(calc(equation))



s
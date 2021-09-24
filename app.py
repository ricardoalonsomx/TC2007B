from flask import Flask
from flask import Flask, request, send_from_directory
from grammar import *
import json

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

#app = Flask(__name__)

@app.route('/')
def initiate(path):
    return send_from_directory('index.htm', path)

@app.route('/<path:equation>')
def index(equation):
    return json.dumps(calc(equation))




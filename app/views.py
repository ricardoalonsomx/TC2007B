from app import app
import json

@app.route('/')
def initiate():
    #return send_from_directory('index.htm', path)
    #return send_from_directory(app.config['index.html'], index.html, as_attachment=True)
    return "hello world"

@app.route('/<path:equation>')
def index(equation):
    return json.dumps(calc(equation))

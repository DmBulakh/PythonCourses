# app.py
from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/method', methods=['POST', 'GET', 'PUT', 'DELETE'])
def request_info():
    return request.method


@app.route('/show_data', methods=['POST'])
def show_date():
    req_data = request.get_json()
    return str(req_data)


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/request')
def request_info1():
    return f'request method: {request.method} url: {request.url} headers: {request.headers}'
# heroku login
# git commit -m
# git push heroku master
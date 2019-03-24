# app.py
from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/method', methods=['GET', 'POST', 'PUT', 'DELETE'])
def request_method():
    return request.method


@app.route('/show_data', methods=['POST'], filename=['*.json'])
def show_date():
    return str(request_info)


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/request')
def request_info():
    return f'request method: {request.method} url: {request.url} headers: {request.headers}'

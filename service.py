import os

from flask import Flask, jsonify

greeting = os.getenv('GREET', 'Hello')

app = Flask(__name__)


@app.route('/')
def greetings():
    return jsonify({'message': greeting})

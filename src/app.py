import os.path
import sys
from flask import Flask, jsonify, json, redirect, url_for, request
import apiai
from flask_cors import CORS

CLIENT_ACCESS_TOKEN = 'f6e375f84c8e418d8c8b7d037d3f0d32'

app = Flask(__name__)
CORS(app)

@app.route('/chat/', methods=['POST', 'GET'])
def chat():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    request = ai.text_request()
    request.session_id = "12345"
    request.query = "number of leaves for this year"
    response = request.getresponse()
    print (response.read())


if __name__ == '__main__':
    app.run(port=8086, host='0.0.0.0')
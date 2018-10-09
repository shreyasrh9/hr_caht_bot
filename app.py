import os.path
import sys
from flask import Flask, jsonify, json, redirect, url_for, request
import apiai
from flask_cors import CORS

CLIENT_ACCESS_TOKEN = ''

app = Flask(__name__)
CORS(app)

@app.route('/chat/', methods=['POST', 'GET'])
def chat():
    req_data = request.get_json()
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    request = ai.text_request()
    request.session_id = "12345"
    request.query = req_data["newMessage"]
    response = request.getresponse()
    return response.read()


if __name__ == '__main__':
    app.run(port=8086, host='0.0.0.0')
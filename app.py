import os.path
import sys
from flask import Flask, request
import apiai
import json
from flask_cors import CORS

CLIENT_ACCESS_TOKEN = 'f6e375f84c8e418d8c8b7d037d3f0d32'

app = Flask(__name__)
CORS(app)

@app.route('/chat/', methods=['POST', 'GET'])
def chat():
    #print("Calling")
    req_data = request.get_json()
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    requestApi = ai.text_request()
    requestApi.session_id = "12345"
    requestApi.query = req_data['newMessage']
    response = requestApi.getresponse()
    #print (response.read())
    return response.read()


if __name__ == '__main__':
    app.run(port=8086, host='0.0.0.0')
# Microservice1 - app.py

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/send_numbers', methods=['POST'])
def send_numbers():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']

    # Send numbers to Microservice2
    response = requests.post('http://m2:5001/add_numbers', json={'num1': num1, 'num2': num2})
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)


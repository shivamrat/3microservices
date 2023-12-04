# Microservice2 - app.py

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/add_numbers', methods=['POST'])
def add_numbers():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']

    # Add numbers and send result to Microservice3
    result = num1 + num2
    response = requests.post('http://m3:5002/multiply_by_15', json={'result': result})
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)


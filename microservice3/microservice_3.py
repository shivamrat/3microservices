# Microservice3 - app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/multiply_by_15', methods=['POST'])
def multiply_by_15():
    data = request.get_json()
    result = data['result']

    # Multiply result by 15
    final_result = result * 15
    
    return jsonify({'final_result': final_result})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002)


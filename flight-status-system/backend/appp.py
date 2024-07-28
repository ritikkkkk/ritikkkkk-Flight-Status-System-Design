from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/flight_status', methods=['GET'])
def get_flight_status():
    with open('mock_flight_data.json') as f:
        flight_data = json.load(f)
    return jsonify(flight_data)

if __name__ == '__main__':
    app.run(debug=True)

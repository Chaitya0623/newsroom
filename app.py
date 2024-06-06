from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Hardcoded password
CORRECT_PASSWORD = "iwannasee"

@app.route('/verify-password', methods=['POST'])
def verify_password():
    data = request.json
    password = data.get('password')
    if password == CORRECT_PASSWORD:
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "fail"}), 401

# if __name__ == '__main__':
#     app.run(debug=True)
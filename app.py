from flask import Flask, jsonify, request
from app.perplexity import talk_to_perplexity

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello, World!"})

@app.route("/run_query", methods=["POST"])
def run_query():
    try:
        request_data = request.get_json()
        print("Received request data:", request_data['query'])
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({'query': request_data['query']})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004, debug=True)
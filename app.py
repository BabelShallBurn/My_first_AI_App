from flask import Blueprint, Flask, jsonify, request
from pydantic import BaseModel, ValidationError
from app.perplexity import talk_to_perplexity

app = Flask(__name__)

class QueryRequest(BaseModel):
    id: str
    query: str

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello, World!"})


@app.route("/run_query", methods=["POST"])
def run_query():
    try:
        request_data = QueryRequest(**request.get_json()) .model_dump()
        print("Received request data:", request_data['query'])
        return jsonify({'query': request_data['query']})
    except ValidationError as error:
        return jsonify(error.errors()), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004, debug=True)
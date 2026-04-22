from flask import Blueprint, request, jsonify
from services.groq_client import get_ai_response

describe_bp = Blueprint("describe", __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()
    user_input = data.get("text")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    result = get_ai_response(user_input)

    return jsonify({"response": result})
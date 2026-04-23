from flask import Blueprint, request, jsonify
from services.groq_client import get_ai_response
from datetime import datetime

describe_bp = Blueprint("describe", __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()

    # ✅ Input validation
    if not data or "text" not in data:
        return jsonify({"error": "Invalid input. 'text' field is required"}), 400

    user_input = data.get("text")

    if not isinstance(user_input, str) or not user_input.strip():
        return jsonify({"error": "Input must be a non-empty string"}), 400

    # ✅ Call AI
    result = get_ai_response(user_input)

    # ✅ Structured response
    return jsonify({
        "input": user_input,
        "response": result,
        "generated_at": datetime.utcnow().isoformat()
    })
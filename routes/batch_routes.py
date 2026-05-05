from flask import Blueprint, request, jsonify
from services.groq_client import get_ai_response
import time

batch_bp = Blueprint("batch", __name__)


@batch_bp.route("/batch-process", methods=["POST"])
def batch_process():
    data = request.get_json()

    
    if not isinstance(data, dict) or "items" not in data:
        return jsonify({"error": "items array required"}), 400

    items = data["items"]

    if not isinstance(items, list):
        return jsonify({"error": "items must be a list"}), 400

    if len(items) == 0:
        return jsonify({"error": "items cannot be empty"}), 400

    if len(items) > 20:
        return jsonify({"error": "max 20 items allowed"}), 400

    results = []

    
    for item in items:
        if not isinstance(item, str) or not item.strip():
            results.append({
                "input": item,
                "error": "invalid input"
            })
            continue

        try:
            response = get_ai_response(item)

            results.append({
                "input": item,
                "output": response
            })

        except Exception as e:
            results.append({
                "input": item,
                "error": str(e)
            })

     
        time.sleep(0.1)

    return jsonify({
        "count": len(results),
        "results": results
    })
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "API is running"

@app.route("/upload-model", methods=["POST"])
def upload_model():
    if "model" not in request.files:
        return jsonify({"error": "No model file uploaded"}), 400
        
    file = request.files["model"]
    try:
        data = json.load(file)
        
        # Prepare response with all necessary fields for the dashboard
        response_data = {
            "accuracy": data.get("accuracy", 0),
            "detail_confusion_matrix": data.get("detail_confusion_matrix", {}),
            "classification_report": data.get("classification_report", {})
        }
        
        # If detail_confusion_matrix is missing, try to get from confusion_matrix array if exists
        if not response_data["detail_confusion_matrix"] and "confusion_matrix" in data:
            cm = data["confusion_matrix"]
            if len(cm) == 2 and len(cm[0]) == 2:
                response_data["detail_confusion_matrix"] = {
                    "TN": cm[0][0],
                    "FP": cm[0][1],
                    "FN": cm[1][0],
                    "TP": cm[1][1]
                }
        
        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)
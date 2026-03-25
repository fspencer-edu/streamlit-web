from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/message", methods=["POST"])
def message():
    data = request.get_json()
    
    user_text = data.get("message", "")
    response = {
        "original_message": user_text,
        "reply": f"Backend received {user_text}"
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
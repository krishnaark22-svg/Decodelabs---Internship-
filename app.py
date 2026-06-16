from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        return "Weak (Too short)"

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    password = data.get("password", "")
    result = check_password_strength(password)
    return jsonify({"strength": result})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
from bot.intent_classifier import IntentClassifier
from bot.rule_engine import rule_based_response

app = Flask(__name__)
clf = IntentClassifier()
clf.train()

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    rule_response = rule_based_response(user_msg)
    if rule_response:
        return jsonify({"response": rule_response})

    tag = clf.predict(user_msg)
    response = clf.get_response(tag)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

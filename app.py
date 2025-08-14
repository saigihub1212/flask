from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"message": "Hello Devops"})


if __name__ == "_main_":
    app.run(host="0.0.0.0", port=5000)
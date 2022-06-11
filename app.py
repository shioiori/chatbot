from flask import Flask, jsonify, render_template, request
from train import get_respond, init

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/", methods=["GET"])

def home():
    return render_template("http://127.0.0.1:5500/static/base.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return jsonify(get_respond(userText))

if __name__ == "__main__":
    init()
    app.debug = "True"
    app.run()
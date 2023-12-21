from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def node():
    return "Home"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Kary",
        "email": "example@exmpl.com"
    }

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
    new = request.args.get("new_one")
    if new:
        user_data["new_one"] = new
    
    return jsonify(user_data), 200

@app.route("/create_user", methods=["POST"])
def create_user():
    data = request.get_json()
    #return jsonify(data), 201
    return ("User " + str(data["user_name"]) + " Created Successfully"), 201 

if __name__== "__main__":
    app.run(debug=True)

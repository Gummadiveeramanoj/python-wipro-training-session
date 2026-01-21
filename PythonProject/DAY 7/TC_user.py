from flask import Flask, jsonify

app1 = Flask(__name__)

users = [
    {"id": 1, "name": "Raja"},
    {"id": 2, "name": "Rama"}
]

@app1.route("/", methods=["GET"])
def home():
    return "Welcome"

@app1.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app1.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"message": "User not found"}), 404

if __name__== "__main__":
    app1.run(debug=True)

@app.route("/users/<int:user_id>",methods=["PUT"])
def update_user(user_id):
    data=request.json
    for user in users:
        if user["id"] == user_id:
            user["name"]=data.get("name")
            return jsonify(user)
    return jsonify({"message": "user not found"}), 404
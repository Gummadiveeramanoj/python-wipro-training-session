from flask import Flask, request, jsonify

app = Flask("__name__")

# In-memory data store
users = [
    {"id": 1, "name": "Raja"},
    {"id": 2, "name": "Rama"}
]

# ---------------------------------
# GET /users → Fetch all users
# ---------------------------------
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# ---------------------------------
# GET /users/<id> → Fetch user by ID
# ---------------------------------
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


# ---------------------------------
# POST /users → Create new user
# ---------------------------------
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    new_id = users[-1]["id"] + 1 if users else 1

    new_user = {
        "id": new_id,
        "name": data["name"]
    }

    users.append(new_user)

    return jsonify({
        "message": "User created successfully",
        "user": new_user
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
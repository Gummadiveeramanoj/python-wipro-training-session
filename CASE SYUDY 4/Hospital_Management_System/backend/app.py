from flask import Flask, request, jsonify

app = Flask(__name__)

patients = []

@app.route("/api/patients", methods=["GET"])
def get_patients():
    return jsonify(patients), 200

@app.route("/api/patients", methods=["POST"])
def add_patient():
    data = request.json
    if not data.get("name") or data.get("age", 0) <= 0:
        return jsonify({"error": "Invalid data"}), 400
    patients.append(data)
    return jsonify(data), 201

@app.route("/api/patients/<int:pid>", methods=["GET"])
def get_patient(pid):
    for p in patients:
        if p.get("id") == pid:
            return jsonify(p), 200
    return jsonify({"error": "Not found"}), 404

@app.route("/api/patients/<int:pid>", methods=["PUT"])
def update_patient(pid):
    for p in patients:
        if p.get("id") == pid:
            p.update(request.json)
            return jsonify(p), 200
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

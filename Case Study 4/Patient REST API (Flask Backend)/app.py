from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
DATA_FILE = "patients.json"


def load_patients():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_patients(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


@app.route("/api/patients", methods=["GET"])
def get_patients():
    return jsonify(load_patients()), 200


@app.route("/api/patients", methods=["POST"])
def add_patient():
    data = request.json
    if not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    patients = load_patients()
    data["id"] = len(patients) + 1
    patients.append(data)
    save_patients(patients)

    return jsonify(data), 201


@app.route("/api/patients/<int:pid>", methods=["GET"])
def get_patient(pid):
    patients = load_patients()
    for p in patients:
        if p["id"] == pid:
            return jsonify(p), 200
    return jsonify({"error": "Patient not found"}), 404


@app.route("/api/patients/<int:pid>", methods=["PUT"])
def update_patient(pid):
    patients = load_patients()
    for p in patients:
        if p["id"] == pid:
            p.update(request.json)
            save_patients(patients)
            return jsonify(p), 200
    return jsonify({"error": "Patient not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

patients = []
pid = 1

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Patient Registration</title></head>
<body>
<h2>Register Patient</h2>
<form method="post" action="/register">
Name: <input name="name"><br>
Age: <input name="age"><br>
Gender:
<input type="radio" name="gender" value="Male"> Male
<input type="radio" name="gender" value="Female"> Female<br>
Contact: <input name="contact"><br>
Disease: <input name="disease"><br>
Doctor:
<select name="doctor">
<option>Dr. Smith</option>
<option>Dr. John</option>
</select><br>
<button type="submit">Submit</button>
</form>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

@app.route("/register", methods=["POST"])
def register():
    global pid
    data = request.form.to_dict()
    data["id"] = pid
    pid += 1
    patients.append(data)
    return "Patient Registered!"

@app.route("/api/patients", methods=["GET"])
def get_patients():
    return jsonify(patients), 200

@app.route("/api/patients", methods=["POST"])
def add_patient():
    global pid
    data = request.json
    data["id"] = pid
    pid += 1
    patients.append(data)
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)
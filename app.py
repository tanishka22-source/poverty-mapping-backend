from flask import Flask, render_template, request, redirect, url_for, jsonify
import datetime

app = Flask(__name__)

# Temporary in-memory storage (GOOD ENOUGH for submission)
reports = []
ngo_status = {}

@app.route("/")
def index():
    # THIS is why you saw nothing earlier
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = {
        "name": request.form.get("name"),
        "location": request.form.get("location"),
        "proof": request.form.get("proof"),
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "risk": "Medium",
        "status": "Pending"
    }
    reports.append(data)
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", reports=reports, ngo_status=ngo_status)

@app.route("/toggle_status/<int:idx>")
def toggle_status(idx):
    if idx < len(reports):
        if reports[idx]["status"] == "Pending":
            reports[idx]["status"] = "Resolved"
        else:
            reports[idx]["status"] = "Pending"
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


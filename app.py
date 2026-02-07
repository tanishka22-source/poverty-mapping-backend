from flask import Flask, render_template, request

app = Flask(__name__)

# Temporary storage (hackathon-friendly)
cases = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    area = request.form["area"]
    income = int(request.form["income"])
    family_size = int(request.form["family_size"])
    emergency = request.form["emergency"]

    score = income / family_size

    if score < 3000:
        risk = "High Urgency"
        color = "red"
        priority = 1
    elif score < 7000:
        risk = "Medium Urgency"
        color = "orange"
        priority = 2
    else:
        risk = "Low Urgency"
        color = "green"
        priority = 3

    case = {
        "area": area,
        "emergency": emergency,
        "score": round(score, 2),
        "risk": risk,
        "color": color,
        "priority": priority
    }

    cases.append(case)

    return render_template("result.html", **case)

@app.route("/dashboard")
def dashboard():
    sorted_cases = sorted(cases, key=lambda x: x["priority"])
    return render_template("dashboard.html", cases=sorted_cases)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


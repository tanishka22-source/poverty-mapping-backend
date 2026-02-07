# List of households (sample data)
households = [
    {"name": "Household A", "income": 8000, "housing": "temporary", "healthcare": "no"},
    {"name": "Household B", "income": 18000, "housing": "permanent", "healthcare": "yes"},
    {"name": "Household C", "income": 6000, "housing": "temporary", "healthcare": "no"},
    {"name": "Household D", "income": 12000, "housing": "temporary", "healthcare": "yes"},
]

# Function to calculate poverty risk score
def calculate_poverty_score(h):
    score = 0

    if h["income"] < 10000:
        score += 30

    if h["housing"] == "temporary":
        score += 20

    if h["healthcare"] == "no":
        score += 20

    return score

# Function to classify risk level
def classify_risk(score):
    if score >= 60:
        return "High"
    elif score >= 30:
        return "Medium"
    else:
        return "Low"

# Process each household
for h in households:
    score = calculate_poverty_score(h)
    risk = classify_risk(score)
    print(h["name"], "→ Score:", score, "| Risk Level:", risk)

from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "data.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"expenses": [], "budgets": {}, "total_budget": 0}, f)

def load_data():
    with open(DATA_FILE) as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/set_total_budget", methods=["POST"])
def set_total_budget():
    data = load_data()
    total_budget = request.json["total_budget"]
    data["total_budget"] = total_budget
    save_data(data)
    return jsonify({"status": "success"})

@app.route("/add_expense", methods=["POST"])
def add_expense():
    data = request.get_json()
    print("Received data:", data)  # Debug line

    if not data or "desc" not in data or "category" not in data or "amount" not in data:
        return jsonify({"error": "Invalid data"}), 400

    with open("data.json", "r") as f:
        saved_data = json.load(f)

    new_expense = {
        "desc": data["desc"],
        "category": data["category"],
        "amount": float(data["amount"])
    }

    saved_data["expenses"].append(new_expense)

    with open("data.json", "w") as f:
        json.dump(saved_data, f, indent=4)

    return jsonify({"message": "Expense added!"}), 200


@app.route("/get_data")
def get_data():
    return jsonify(load_data())

if __name__ == "__main__":
    app.run(debug=True)

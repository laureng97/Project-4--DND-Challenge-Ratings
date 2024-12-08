from flask import Flask, render_template, request
import pandas as pd
import joblib

# Set the current directory as the template folder
app = Flask(__name__, template_folder=".")

# Load your trained model
model = joblib.load("linear_model.pkl")

@app.route("/", methods=["GET"])
def home():
    """Home route to render the form."""
    return render_template("index.html", prediction=None, error=None)

@app.route("/predict", methods=["POST"])
def predict():
    """Route to handle predictions."""
    try:
        # Collect form data
        input_data = pd.DataFrame({
            "name": [request.form.get("name", "")],
            "size": [request.form.get("size", "")],
            "type": [request.form.get("type", "")],
            "alignment": [request.form.get("alignment", "")],
            "armor_class": [int(request.form.get("armor_class", 0))],
            "hit_points": [int(request.form.get("hit_points", 0))],
            "hit_dice": [request.form.get("hit_dice", "")],
            "speed": [request.form.get("speed", "")],
            "strength": [int(request.form.get("strength", 0))],
            "dexterity": [int(request.form.get("dexterity", 0))],
            "constitution": [int(request.form.get("constitution", 0))],
            "intelligence": [int(request.form.get("intelligence", 0))],
            "wisdom": [int(request.form.get("wisdom", 0))],
            "charisma": [int(request.form.get("charisma", 0))],
            "proficiencies": [request.form.get("proficiencies", "")],
            "damage_vulnerabilities": [request.form.get("damage_vulnerabilities", "")],
            "damage_resistances": [request.form.get("damage_resistances", "")],
            "damage_immunities": [request.form.get("damage_immunities", "")],
            "condition_immunities": [request.form.get("condition_immunities", "")],
            "senses": [request.form.get("senses", "")],
            "special_abilities": [request.form.get("special_abilities", "")],
            "actions": [request.form.get("actions", "")],
            "legendary_actions": [request.form.get("legendary_actions", "")],
            "reactions": [request.form.get("reactions", "")],
            "other_speeds": [request.form.get("other_speeds", "")]
        })

        # Make predictions using the loaded model
        prediction = model.predict(input_data)[0]

        # Render the result
        return render_template("index.html", prediction=round(prediction, 2), error=None)
    except Exception as e:
        # Handle errors gracefully and show them on the page
        return render_template("index.html", prediction=None, error=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# -------------------------------
# Load trained ML model
# -------------------------------
with open("../model/nutrition_model.pkl", "rb") as file:
    model = pickle.load(file)

# -------------------------------
# Load food nutrition dataset
# -------------------------------
food_df = pd.read_csv("../data/food_nutrition.csv")

# -------------------------------
# Meal recommendation logic
# -------------------------------
def recommend_meal(status):
    if status == "Underweight":
        # High calorie foods
        return food_df[food_df["calories"] > 180]
    elif status == "Overweight":
        # Low calorie foods
        return food_df[food_df["calories"] < 150]
    else:
        # Balanced foods
        return food_df[
            (food_df["calories"] >= 120) & (food_df["calories"] <= 200)
        ]

# -------------------------------
# Home route
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -------------------------------
# Prediction route
# -------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    # Get form data
    age = int(request.form["age"])
    gender = int(request.form["gender"])
    height = float(request.form["height"])
    weight = float(request.form["weight"])
    activity = int(request.form["activity"])

    # BMI calculation
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    # Prepare features for model
    features = np.array([[age, gender, height, weight, activity, bmi]])

    # Predict nutrition status
    prediction = model.predict(features)[0]

    # Map encoded output to labels
    result_map = {
        0: "Normal",
        1: "Overweight",
        2: "Underweight"
    }

    result = result_map.get(prediction, "Unknown")

    # Get meal recommendations
    recommended_foods = recommend_meal(result)
    meals = recommended_foods[["food", "category"]].to_dict(orient="records")

    return render_template(
        "result.html",
        result=result,
        meals=meals
    )

# -------------------------------
# Run the app
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)

# AI-Driven Nutritional Assessment and Personalized Meal Planning for Children

## Overview
This project presents an AI-driven system that assesses children's nutritional status using machine learning and provides personalized meal recommendations. The system analyzes health parameters such as age, height, weight, and activity level to classify the nutritional condition and suggest appropriate meals.

The application is built using a Machine Learning model integrated with a Flask-based web interface.

---

## Problem Statement
Many children experience nutritional imbalance due to lack of personalized dietary assessment. Traditional diet recommendations are often generalized and do not consider individual health parameters such as BMI, activity level, and growth indicators.

This project aims to provide a data-driven solution for assessing nutritional status and generating personalized meal plans.

---

## Objectives
- Develop a machine learning model to classify children's nutritional status.
- Calculate BMI and analyze health indicators.
- Provide personalized meal recommendations.
- Build a user-friendly web-based system for interaction.

---

## Technologies Used
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML/CSS

---

## Machine Learning Model
The system uses a **Decision Tree Classifier** to predict nutritional status based on the following features:

- Age
- Gender
- Height
- Weight
- Activity Level
- BMI

The model classifies children into categories such as:
- Underweight
- Normal
- Overweight

---

## System Architecture

User Input (Web Form)  
↓  
Flask Backend  
↓  
Machine Learning Model (Decision Tree)  
↓  
Prediction of Nutritional Status  
↓  
Meal Recommendation System  
↓  
Display Results to User

---

## Dataset
The dataset contains structured health data including:

- Age
- Gender
- Height (cm)
- Weight (kg)
- Activity Level
- Nutritional Status

The dataset is used to train the machine learning model.

---

## Features
- Nutritional status prediction
- BMI calculation
- Personalized meal recommendations
- Simple web interface for user interaction
- Machine learning based classification

---

## Project Structure

AI_Nutrition_Project
│
├── app
│ ├── app.py
│ ├── templates
│ │ ├── index.html
│ │ └── result.html
│
├── data
│ ├── child_health.csv
│ └── food_nutrition.csv
│
├── model
│ └── nutrition_model.pkl
│
├── notebooks
│ └── model_training.ipynb
│
└── README.md

---

## How to Run the Project

### Step 1: Clone the repository

git clone <repository-url>

### Step 2: Navigate to project folder

cd AI_Nutrition_Project

### Step 3: Activate virtual environment

.\.venv\Scripts\activate

### Step 4: Run the Flask application

cd app
python app.py

### Step 5: Open browser

http://127.0.0.1:5000/

## Future Improvements
- Larger dataset for improved model accuracy
- Advanced machine learning models
- Mobile-friendly interface
- Integration with real nutrition databases

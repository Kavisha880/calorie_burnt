🏃‍♂️ Calorie Burn Prediction Web Application


This Flask-based web application predicts the number of calories burned during physical activities based on user inputs such as gender, age, height, weight, duration, heart rate, and body temperature. The application leverages a machine learning model trained on a comprehensive dataset to provide accurate estimations.

📋 Table of Contents
Introduction

Features

Dataset

Installation

Usage

Model Details

Contributing

License

📌 Introduction
Understanding the number of calories burned during exercise is crucial for individuals aiming to manage their health and fitness. This project utilizes machine learning algorithms to provide accurate calorie burn predictions based on physiological and activity-related parameters.

✨ Features
Predicts calories burned based on user input parameters.

Interactive and user-friendly web interface built with Flask.

Data preprocessing and model training capabilities.

Clear visualization of results.

📊 Dataset
The dataset used in this project comprises 15,000 samples, including features such as:

Gender

Age

Height

Weight

Duration of exercise

Heart rate

Body temperature

Calories burned

Note: Ensure you have the appropriate rights to use and share the dataset if you plan to make this repository public.

🛠️ Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/calorie-burn-prediction.git
cd calorie-burn-prediction
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
🚀 Usage
Run the Flask application:

bash
Copy
Edit
python app.py
Access the application:

Open your web browser and navigate to http://localhost:5000.

Input your data:

Enter the required information such as age, gender, weight, height, duration, heart rate, and body temperature.

View results:

Click on the "Predict" button to see the estimated calories burned.

🧠 Model Details
Algorithm Used: Random Forest Regressor

Training Accuracy: 95%

Testing Accuracy: 93%

Evaluation Metrics: Mean Absolute Error (MAE), Mean Squared Error (MSE), R² Score


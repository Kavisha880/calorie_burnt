from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('calories_burnt.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')  
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    gender = int(request.form['gender'])       # 0 = male, 1 = female
    age = int(request.form['age'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    duration = float(request.form['duration'])
    heart_rate = float(request.form['heart_rate'])
    body_temp = float(request.form['body_temp'])

    # Model expects input as 2D array
    input_data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])

    # Predict calories burnt
    result = model.predict(input_data)[0]

    return render_template('index.html', result=round(result, 2))

if __name__ == '__main__':
    app.run(debug=True) 

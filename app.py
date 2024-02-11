from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction import CustomData, PredictPipeline

# Initialize Flask application
application = Flask(__name__)
app = application

# Define route for the home page
@app.route('/')
def index():
    # Define route for the home page
    # for this we create a folder templates and add index.html to it
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        # contains the simple input fields that are needed for prdiction
        # For GET request, show the data input form
        return render_template('home.html')
    
    else:
        # For POST request, process form data for prediction
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),  # Possible mix-up here
            writing_score=float(request.form.get('reading_score'))  # Possible mix-up here
        )

        # Convert data to DataFrame for the prediction model
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        # Initialize prediction pipeline
        predict_pipeline = PredictPipeline()
        print("Mid Prediction")

        # Make predictions
        results = predict_pipeline.predict(pred_df)
        print("after Prediction")

        # Render the template with prediction results
        return render_template('home.html', results=results[0])
    
    
# Run the Flask application if this is the main program
if __name__ == "__main__":
    app.run(host="0.0.0.0")  # Makes the server publicly available
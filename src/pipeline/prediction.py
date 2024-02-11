import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:

    def __init__(self):
        pass

    def predict(self, features):   
        """Predicts outcomes based on input features using a pre-trained model and preprocessor."""
        try:
            # Paths to the saved model and preprocessor
            model_path= os.path.join("artifacts","model.pkl")
            preprocessor_path= os.path.join('artifacts','proprocessor.pkl')
            print("Before Loading")

             # Load the model and preprocessor
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path =preprocessor_path)
            print("After Loading")

            # Apply preprocessor to the input features
            data_scaled = preprocessor.transform(features)
            print(data_scaled)

            # Predict outcomes using the processed features
            preds = model.predict(data_scaled)
            print(preds)

            return preds
        except Exception as e:
            return CustomException(e, sys)

class CustomData:
    # We use this class to get the data from the flask application 

    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):
        """Initializes with data for a single observation."""

        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        """Converts the input data into a pandas DataFrame."""
        try:
            # Create a dictionary from the input data
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            # Convert the dictionary to a DataFrame
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)
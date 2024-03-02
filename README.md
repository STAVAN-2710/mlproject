# ML Project

Welcome to the ML Project repository. This project is structured to provide an end-to-end machine learning solution, incorporating aspects from data ingestion to model training and prediction. It leverages MLflow for tracking experiments, demonstrating the application of various machine learning algorithms to predict student performance.

## Project Overview

The application predicts student performance based on several factors, including gender, race/ethnicity, parental level of education, lunch type, and test preparation course status. It showcases the use of Flask for the web interface, allowing users to input student characteristics and receive a performance prediction.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- MLflow
- Various Python packages (pandas, numpy, scikit-learn, etc.)

### Installation

1. Clone the repository:
git clone https://github.com/STAVAN-2710/mlproject.git

2. Install the required Python packages:
pip install -r requirements.txt

### Running the Application

To start the Flask application:
python app.py

This will host the application on `http://localhost:8080`, where you can interact with the prediction model through a simple web interface.

## Project Structure

- `app.py`: Entry point for the Flask application.
- `requirements.txt`: Specifies the Python packages required to run the project.
- `setup.py`: Setup script for installing the project package.
- `src/`: Contains the core logic for data ingestion, transformation, and model training.
- `notebooks/data/`: Jupyter notebooks for exploratory data analysis and model training.
- `templates/`: HTML templates for the Flask application.
- `.github/workflows/`: Contains GitHub Actions workflows for CI/CD.

## Usage

The web application allows users to input data through a form and receive a prediction for student performance. The prediction model is trained on a dataset that includes various student attributes and their corresponding performance outcomes.



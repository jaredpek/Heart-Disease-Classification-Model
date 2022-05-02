# Heart-Disease-ML-Model
Project Description:
- This is a Machine Learning Model Created using Python's SciKit-Learn Library.
- The model will predict whether a person has Heart Disease from their Medical Attributes.
- Refer to the ProjectOverview File for more information.

Installation:
1. Download Project:
    - git clone https://github.com/jaredpek/Heart-Disease-ML-Model
2. Install Requirements:
    - pip install -r requirements.txt

Loading the Model:
1. Import the Load function from Joblib Library:
    - from joblib import load
2. Load Heart Disease Model:
    - heartDiseaseModel = load(filename='HeartDiseaseModel.joblib')
3. Model would be successfully loaded
    - Can use it to:
        - Improve HyperParameters,
        - Predict Heart Disease etc.

Saving the Model:
1. Import the Save function from Joblib Library:
    - from joblib import save
2. Save Heart Disease Model:
    - save({Name of Heart Disease Model Variable}, filename='HeartDiseaseModel')
3. Model would be saved in the same directory

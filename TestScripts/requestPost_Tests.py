# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 23:57:50 2022

@author: choareau
"""
def test_predict():
  
  import sys
  sys.path.insert(0, 'Backend/Model/src/')
  import modelAPI 

  correctDataFormat = {
    'gender': 'Male',
    'SeniorCitizen': 'Yes',
    'Partner': 'Yes',
    'Dependents': 'Yes',
    'tenure': 0,
    'PhoneService': 'Yes',
    'MultipleLines': 'Yes',
    'InternetService': 'No',
    'OnlineSecurity': 'No internet service',
    'OnlineBackup': 'No internet service',
    'DeviceProtection': 'No internet service',
    'TechSupport': 'No internet service',
    'StreamingTV': 'No internet service',
    'StreamingMovies': 'No internet service',
    'Contract': 'Two year',
    'PaperlessBilling': 'Yes',
    'PaymentMethod': 'Credit card (automatic)',
    'MonthlyCharges': 0,
    'TotalCharges': 0
  }

  listValue = ['Yes', 'No']
  b = modelAPI.get_prediction(correctDataFormat)
  assert b in listValue

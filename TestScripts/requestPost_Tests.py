# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 23:57:50 2022

@author: choareau
"""
def testModelPrediction():
  
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
  
  # Check if Model API returns expected value
  modelResponse = modelAPI.get_prediction(correctDataFormat)
  assert modelResponse in listValue
  
#def testWebToModelConnection():
#  
#  import sys
#  sys.path.insert(0, 'Backend/Model/src/')
#  sys.path.insert(0, 'Backend/Web/src/')
#  import modelAPI
#  import webAPI
#
#  correctDataFormat = {
#    'gender': 'Male',
#    'SeniorCitizen': 'Yes',
#    'Partner': 'Yes',
#    'Dependents': 'Yes',
#    'tenure': 0,
#    'PhoneService': 'Yes',
#    'MultipleLines': 'Yes',
#    'InternetService': 'No',
#    'OnlineSecurity': 'No internet service',
#    'OnlineBackup': 'No internet service',
#    'DeviceProtection': 'No internet service',
#    'TechSupport': 'No internet service',
#    'StreamingTV': 'No internet service',
#    'StreamingMovies': 'No internet service',
#    'Contract': 'Two year',
#    'PaperlessBilling': 'Yes',
#    'PaymentMethod': 'Credit card (automatic)',
#    'MonthlyCharges': 0,
#    'TotalCharges': 0
#  }
#
#  listValue = ['Yes', 'No']
#  
#  # Check if Web API returns expected value
#  webResponse = webAPI.get_prediction(correctDataFormat)
#  assert webResponse in listValue

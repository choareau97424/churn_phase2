# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 23:57:50 2022

@author: choareau
"""
def testModelPrediction():
  
  import sys
  sys.path.insert(0, 'Backend/Model/src/')
  sys.path.insert(0, 'Backend/Data/src/')
  import modelAPI 
  import dataAPI 

  correctDataFormatModel = {
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
  
  correctDataFormatData = {
    'customerID': '1234-ABCDE',
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
    'TotalCharges': 0,
    'Churn': 'Yes',
    'ChurnPrediction': 'Yes'
  }

  listValue = ['Yes', 'No']
  
  # Check if Model API returns expected value
  modelResponse = modelAPI.get_prediction(correctDataFormatModel)
  assert modelResponse in listValue
  
  # Check if Data API returns expected value
  dataResponse = dataAPI.save_data(correctDataFormatModelData)
  assert dataResponse == 'New entry saved'
  
#def testWebToModelConnection():
#  
#  import sys
#  sys.path.insert(0, 'Backend/Model/src/')
#  sys.path.insert(0, 'Backend/Data/src/')
#  import modelAPI
#  import dataAPI
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

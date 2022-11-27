import sys
sys.path.insert(0, 'Backend/Model/src/')
sys.path.insert(0, 'Backend/Data/src/')
import modelAPI 
import dataAPI 
import pytest
#  
@pytest.mark.testModelPrediction
def testModelPrediction():
  
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
  
  listValue = ['Yes', 'No']
  
  # Check if Model API returns expected value
  modelResponse = modelAPI.get_prediction(correctDataFormatModel)
  assert modelResponse in listValue
  
  
  
@pytest.mark.testDataSaving  
def testDataSaving():
  
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
  
  # Check if Data API returns expected value
  dataResponse = dataAPI.save_data(correctDataFormatData)
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

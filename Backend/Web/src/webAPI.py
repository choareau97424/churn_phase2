# -*- coding: utf-8 -*-


# Import required modules
import requests
import random  
import string 
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
from fastapi.encoders import jsonable_encoder

# from fastapi import Depends, HTTPException
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
# from starlette.status import HTTP_401_UNAUTHORIZED

def generateCustomerID(): 
    result = ''.join((random.choice(string.ascii_uppercase) for x in range(5)))  
    result1 = ''.join((random.choice(string.digits) for x in range(4))) 
    return result1 + '-' + result


## Schema validation
class Features(BaseModel):
    gender: Literal['Male', 'Female']
    SeniorCitizen: Literal['Yes', 'No']
    Partner: Literal['Yes', 'No']
    Dependents: Literal['Yes', 'No']
    tenure: int
    PhoneService: Literal['Yes', 'No']
    MultipleLines: Literal['Yes', 'No', 'No phone service']
    InternetService: Literal['No', 'Fiber optic', 'DSL']
    OnlineSecurity: Literal['No internet service', 'No', 'Yes']
    OnlineBackup: Literal['No internet service', 'No', 'Yes']
    DeviceProtection: Literal['No internet service', 'No', 'Yes']
    TechSupport: Literal['No internet service', 'No', 'Yes']
    StreamingTV: Literal['No internet service', 'No', 'Yes']
    StreamingMovies: Literal['No internet service', 'No', 'Yes']
    Contract: Literal['Two year', 'Month-to-month', 'One year']
    PaperlessBilling: Literal['Yes', 'No']
    PaymentMethod: Literal['Credit card (automatic)', 'Bank transfer (automatic)', 'Mailed check', 'Electronic check']
    MonthlyCharges: float
    TotalCharges: float
    
# data = {
#   'gender': 'Male',
#   'SeniorCitizen': 'Yes',
#   'Partner': 'Yes',
#   'Dependents': 'Yes',
#   'tenure': 0,
#   'PhoneService': 'Yes',
#   'MultipleLines': 'Yes',
#   'InternetService': 'No',
#   'OnlineSecurity': 'No internet service',
#   'OnlineBackup': 'No internet service',
#   'DeviceProtection': 'No internet service',
#   'TechSupport': 'No internet service',
#   'StreamingTV': 'No internet service',
#   'StreamingMovies': 'No internet service',
#   'Contract': 'Two year',
#   'PaperlessBilling': 'Yes',
#   'PaymentMethod': 'Credit card (automatic)',
#   'MonthlyCharges': 0,
#   'TotalCharges': 0
# }

# data1 = Features(
#     gender= 'Male',
#     SeniorCitizen= 'Yes',
#   Partner= 'Yes',
#   Dependents= 'Yes',
#   tenure= 0,
#   PhoneService= 'Yes',
#   MultipleLines= 'Yes',
#   InternetService= 'No',
#   OnlineSecurity= 'No internet service',
#   OnlineBackup= 'No internet service',
#   DeviceProtection= 'No internet service',
#   TechSupport= 'No internet service',
#   StreamingTV= 'No internet service',
#   StreamingMovies= 'No internet service',
#   Contract= 'Two year',
#   PaperlessBilling= 'Yes',
#   PaymentMethod= 'Credit card (automatic)',
#   MonthlyCharges= 0,
#   TotalCharges= 0
# )

# Instantiate the HTTPBasic module for Authentication
#security = HTTPBasic()

# definition of the API address
api_address_model = '172.50.0.2'
api_address_data = '172.50.0.4'
# API port
api_port_model = '8000'
api_port_data = '8002'

# Instantiate the FastAPI module
api = FastAPI(
    title="Churn Project",
    description="Objective : Request a model API to get churn prediction" + 
    "by Author : C. Hoareau / W. Siounandan",
    version="1.0.0"
    )

# Definition of Authorized API functions Users (login + password)
authorizedUsers = {
    "christophe": "admin",
    "william": "admin"
}

# Just check that the API works
@api.get('/', name='About WEB API Status', tags=['Public'])
def home():
    return {
        'Status OK'
    }

# Get all questions for the selected test type and sort them randomly
@api.post('/prediction', name='Get the prediction from the MODEL API', tags=['Public'])
async def get_prediction(data: Features):

    try:
        encData = jsonable_encoder(data)
        newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(
            url='http://{address}:{port}/prediction'.format(address=api_address_model, port=api_port_model), 
            json=encData,
            headers=newHeaders)

        dictData = data.dict()
        df = pd.DataFrame.from_dict([dictData])
        df['Churn'] = 'Undefined'
        df['ChurnPrediction'] = r.json()
        df['customerID'] = generateCustomerID()
        first_column = df.pop('customerID')
        df.insert(0,'customerID', first_column)
        
        encData_w_pred = df.to_dict('records')
        encData_w_pred1 = jsonable_encoder(encData_w_pred[0])
        newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        t = requests.post(
            url='http://{address}:{port}/databackup'.format(address=api_address_data, port=api_port_data), 
            json=encData_w_pred1,
            headers=newHeaders)
        t.json()
        
        return r.json()
    
    except IndexError:
        return {}
    
# -*- coding: utf-8 -*-

# Import required modules
import os
import pandas as pd
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from typing import Literal
from pydantic import BaseModel


## Schema validation
class Features(BaseModel):
    customerID : str
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
    Churn: str  
    ChurnPrediction : Literal['Yes', 'No']
  
# Instantiate the FastAPI module
api = FastAPI(
    title="Churn Project",
    description="Objective : Save new record into the csv file" + 
    "by Author : C. Hoareau / W. Siounandan",
    version="1.0.0"
    )

# Just check that the API works
@api.get('/', name='About DATA API Status', tags=['Public'])
def home():
    return {
        'Status OK'
    }

# Get all questions for the selected test type and sort them randomly
@api.post('/databackup/', name='Save the new entry and corresponding prediction into a csv file', tags=['Public'])
async def save_data(data: Features):

    try:
        
        dictData = jsonable_encoder(data)
        for key, value in dictData.items():
            dictData[key] = [value]
        
        newEntry = pd.DataFrame.from_dict(dictData)
        if (os.path.isfile('/data/churn.csv')):
            newEntry.to_csv('/data/churn.csv', mode='a', index=False, header=False)
        else:
            newEntry.to_csv('/data/churn.csv', index=False)
        
        return  "New entry saved"       

    except IndexError:
        return {}
    

# -*- coding: utf-8 -*-

import requests
from fastapi.encoders import jsonable_encoder


# ## Schema validation
# class Features(BaseModel):
#     customerID : str
#     gender: Literal['Male', 'Female']
#     SeniorCitizen: Literal['Yes', 'No']
#     Partner: Literal['Yes', 'No']
#     Dependents: Literal['Yes', 'No']
#     tenure: int
#     PhoneService: Literal['Yes', 'No']
#     MultipleLines: Literal['Yes', 'No', 'No phone service']
#     InternetService: Literal['No', 'Fiber optic', 'DSL']
#     OnlineSecurity: Literal['No internet service', 'No', 'Yes']
#     OnlineBackup: Literal['No internet service', 'No', 'Yes']
#     DeviceProtection: Literal['No internet service', 'No', 'Yes']
#     TechSupport: Literal['No internet service', 'No', 'Yes']
#     StreamingTV: Literal['No internet service', 'No', 'Yes']
#     StreamingMovies: Literal['No internet service', 'No', 'Yes']
#     Contract: Literal['Two year', 'Month-to-month', 'One year']
#     PaperlessBilling: Literal['Yes', 'No']
#     PaymentMethod: Literal['Credit card (automatic)', 'Bank transfer (automatic)', 'Mailed check', 'Electronic check']
#     MonthlyCharges: float
#     TotalCharges: float
#     Churn: str  
#     ChurnPrediction : Literal['Yes', 'No']
    

# data = Features(
#     customerID= '1234-ABCDE',
#     gender= 'Male',
#     SeniorCitizen= 'Yes',
#     Partner= 'Yes',
#     Dependents= 'Yes',
#     tenure= 0,
#     PhoneService= 'Yes',
#     MultipleLines= 'Yes',
#     InternetService= 'No',
#     OnlineSecurity= 'No internet service',
#     OnlineBackup= 'No internet service',
#     DeviceProtection= 'No internet service',
#     TechSupport= 'No internet service',
#     StreamingTV= 'No internet service',
#     StreamingMovies= 'No internet service',
#     Contract= 'Two year',
#     PaperlessBilling= 'Yes',
#     PaymentMethod= 'Credit card (automatic)',
#     MonthlyCharges= 0,
#     TotalCharges= 0,
#     Churn= 'Undefined',  
#     ChurnPrediction= 'No'
# )

data = {
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

# definition of the API address
api_address_model = '127.0.0.1'
# API port
api_port_model = '8000'

encData = jsonable_encoder(data);
newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}

try: 
    r = requests.post(
        url='http://{address}:{port}/prediction'.format(address=api_address_model, port=api_port_model), 
        json=encData,
        headers=newHeaders)
    statusCode = r.status_code
    msgToDisplay = r.text
except requests.exceptions.ConnectionError:
    try: r
    except NameError: 
        statusCode = 503
        msgToDisplay = 'HTTP Connection Error'
    

if statusCode == 200:
    testStatus = 'SUCCESS'
else:
    testStatus = 'FAILURE'
        
outputStr = '''
    ==============================
    Get Prediction from Model test
    ==============================
    request done at "/prediction"
    expected result = 200
    actual result = {statusCode}
    ==>  {testStatus}
    {text}\n\n'''.format(statusCode=statusCode,testStatus=testStatus,text=msgToDisplay)    
            
# printing in a file
if 1:#os.environ.get('LOG') == 1:
    with open('./log/api_test.log', 'a') as file:
        file.write(outputStr)
        


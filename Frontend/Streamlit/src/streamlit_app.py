# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import requests
from PIL import Image
from fastapi.encoders import jsonable_encoder


# definition of the API address
api_address_web = '172.50.0.3'
# API port
api_port_web = '8001'

# this is a comment
def main():
    
    st.sidebar.info('This app is created in the framework of the Customer Churn Project')
    
    image = Image.open('Images/churn_01.png') 
    st.image(image,use_column_width=False) 
    
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
    
    
    st.subheader("About the Customer")
    col1_cust, col2_cust = st.columns(2)
    with col1_cust:
        gender = st.selectbox('Gender:', ('Male', 'Female'))
        SeniorCitizen= st.selectbox('Senior Citizen:', ('Yes', 'No'))
    with col2_cust:
        Partner= st.selectbox('Partner:', ('Yes', 'No'))
        Dependents = st.selectbox('Dependents:', ('Yes', 'No'))
        
    st.subheader("About the Services")    
    col1_serv, col2_serv, col3_serv = st.columns(3)
    with col1_serv:
        PhoneService = st.selectbox('Phone Service:', ('Yes', 'No'))
        MultipleLines = st.selectbox('Multiple Lines:', ('Yes', 'No', 'No phone service'))
        InternetService= st.selectbox('Internet Service:', ('No', 'Fiber optic', 'DSL'))
    with col2_serv:
        OnlineSecurity= st.selectbox('Online Security:', ('Yes', 'No', 'No internet service'))
        OnlineBackup = st.selectbox('Online Backup:', ('Yes', 'No', 'No internet service'))
        DeviceProtection = st.selectbox('Device Protection:', ('Yes', 'No', 'No internet service'))
    with col3_serv:
        TechSupport = st.selectbox('Technical Support:', ('Yes', 'No', 'No internet service'))
        StreamingTV = st.selectbox('Streaming TV:', ('Yes', 'No', 'No internet service'))
        StreamingMovies = st.selectbox('Streaming Movies:', ('Yes', 'No', 'No internet service'))
        
    st.subheader("About the Contract")    
    col1_cont, col2_cont, col3_cont = st.columns(3)
    with col1_cont:
        tenure = st.number_input('Tenure:', min_value=0, max_value=240, value=0)   
        Contract= st.selectbox('Contract Type:', ('Two year', 'Month-to-month', 'One year'))
    with col2_cont:
        PaperlessBilling = st.selectbox('Paperless Billing:', ('Yes', 'No'))
        PaymentMethod= st.selectbox('Payment Method:', ('Credit card (automatic)', 'Bank transfer (automatic)', 'Mailed check', 'Electronic check'))
    with col3_cont:
        MonthlyCharges= st.number_input('Monthly Charges:', min_value=0, max_value=240, value=0)
        TotalCharges = tenure*MonthlyCharges
    
    data = {
      'gender': gender,
      'SeniorCitizen': SeniorCitizen,
      'Partner': Partner,
      'Dependents': Dependents,
      'tenure': tenure,
      'PhoneService': PhoneService,
      'MultipleLines': MultipleLines,
      'InternetService': InternetService,
      'OnlineSecurity': OnlineSecurity,
      'OnlineBackup': OnlineBackup,
      'DeviceProtection': DeviceProtection,
      'TechSupport': TechSupport,
      'StreamingTV': StreamingTV,
      'StreamingMovies': StreamingMovies,
      'Contract': Contract,
      'PaperlessBilling': PaperlessBilling,
      'PaymentMethod': PaymentMethod,
      'MonthlyCharges': MonthlyCharges,
      'TotalCharges': TotalCharges
    }

    col1_tmp, col2_tmp, col3_tmp = st.columns(3)
    with col3_tmp:
        if st.button("Predict"):
            
            encData = jsonable_encoder(data)
            newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            r = requests.post(
                url='http://{address}:{port}/prediction'.format(address=api_address_web, port=api_port_web), 
                json=encData,
                headers=newHeaders)
            
            st.success(r.json())

    df = pd.read_csv('/data/churn.csv')    
    # dictData = jsonable_encoder(data)
    # for key, value in dictData.items():
    #     dictData[key] = [value]
    
    # df = pd.DataFrame.from_dict(dictData)
    csv = df.to_csv(index=False)
    st.sidebar.download_button(
        label="📥 Download data as CSV",
        data=csv,
        file_name='churn_downloadedData.csv',
        mime='text/csv',
    )    

if (__name__ == '__main__'):
    main()

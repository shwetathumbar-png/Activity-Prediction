
import streamlit as st
import numpy as np
import pandas as pd
import joblib

with open('final_model.joblib','rb') as file:
    model = joblib.load(file)
    
def prediction(inp_list):
    
    pred = model.predict([inp_list])[0]
    if pred == 0:
        return 'Sitting on bed'
    elif pred == 1:
        return 'Sitting on Chair'
    elif pred == 2:
        return 'Lying on bed'
    else:
        'Ambulating'

def main():
    st.title('ACTIVITY PREDICTION FROM SENSOR DATA')
    st subheader('''This application will predict the on going activity of the besis of sensor data provided. 
                 Fill the respective fields it will be predicted.''')
    st.image('image.png')
    
    rfid = st.dropbox('Enter the RFID configuration settings',['config 1 (4 sensors)','config 2 (3 sensors)'])
    rfid_e = (lambda x: 3 if x=='config 2 (3 sensors)' else 4)(rfid)
    
    ant_ID = st.dropbox('select the Antena ID',[1,2,3,4])
    rssi = st.text_input('Enter the received signal strength indicator (RSSI)')
    accv = st.text_input('Enter the vertical acceleration data from sensor')
    accf = st.text_input('Enter the frontal acceleration data from sensor')
    accl = st.text_input('Enter the lateral acceleration data from sensor')
    
    inp_data = [accf,accv,accl,ant_ID,rssi,rfid_e]
    
    if st.button('predict'):
        response = prediction(inp_data)
        st.success(response)
        
if __name__=='__main__':
    main()
    

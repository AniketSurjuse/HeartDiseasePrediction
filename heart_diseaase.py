# -*- coding: utf-8 -*-
"""
Created on Sun May  7 23:36:14 2023

@author: LINOVA
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open(r"C:\Users\LINOVA\Desktop\Heart Disease\heart_disease_prediction.pckl","rb"))

def heart_disease_prediction(input_data):
    input_data_np_array = np.array(input_data)
    
    reshaped_input_data = input_data_np_array.reshape(1,-1)
    
    prediction = loaded_model.predict(reshaped_input_data)
    
    if prediction[0]==1:
        return "You might have heart disease"
    else:
        return "You do NOT have heart disease"
    
    

def main():
    st.title("Heart Disease Prediction Web App")
    
    #age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal	target
    age = st.text_input("Age")
    sex = st.text_input("Gender")
    cp = st.text_input("cp")
    trestbps = st.text_input("Trestbps")
    chol = st.text_input("chol level")
    fbs = st.text_input("fbs")
    restecg = st.text_input("restecg")
    thalach = st.text_input("thalach")
    exang = st.text_input("exang")
    oldpeak = st.text_input("oldpeak")
    slope = st.text_input("slope")
    ca = st.text_input("ca")
    thal = st.text_input("thal")
     
    result = ""
    if st.button("Get your Result"):
        result = heart_disease_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
         
    st.success(result)     


if __name__ =='__main__':
    main()    
         
         
         
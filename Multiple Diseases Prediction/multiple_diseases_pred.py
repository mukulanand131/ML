# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 19:55:05 2023

@author: mukul
"""
# Importing dependencies
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved model

diabetes_model = pickle.load(open('C:/Users/mukul/OneDrive/Documents/one drive backup/Desktop/Multiple Diseases Prediction/Saved Models/Diabetes_Multiple_Disease_Prediction_model.sav', 'rb'))

heart_model = pickle.load(open('C:/Users/mukul/OneDrive/Documents/one drive backup/Desktop/Multiple Diseases Prediction/Saved Models/heart_model.sav', 'rb'))
# Creating the sidebars for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',                    # Title of the Sidebar
                           ['Diabetes Prediction','Heart Disease Prediction'],      # Name of individual pages
                           
                           icons = ['activity','heart'],                            # Icons for the name of individual pages
                           
                           default_index = 0)                                       # To load the Diabetes Prediction as default page
    
    
    

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    # Page title
    st.title('Diabetes Prediction using ML')
    
    # Getting the input data from the user
    # Column for input
    # st.text_input will create a input fields with the help of streamlit library
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')
    
    # Code for prediction
    diab_diagnosis = ''              # To store the final result
    
    # Creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_diagnosis = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])           # We are inclosing input values in two [[[]]] to make the model understand that the model will predict for only one instance.
        
        
        # Showing Result of prediction.
        if(diab_diagnosis[0] == 1):
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is Non Diabetic'
            
    st.success(diab_diagnosis)       # To display the result.

    

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    # Page title
    st.title('Heart Disease Prediction using ML')
    
    # Getting the input data from the user
    # Column for input
    # st.text_input will create a input fields with the help of streamlit library
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age of the person')
    with col2:
        sex = st.text_input('Sex of the person')
    with col3:
        cp = st.text_input('Chest Pain(CP) types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dL')
    with col3:
         fbs = st.text_input('Fasting Blood Sugar > 120 mg/dL')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels coloured by flaurosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
    # Code for prediction
    heart_diagnosis = ''              # To store the final result
    
    # Creating a button for prediction
    if st.button('Heart Disease Test Result'):
        heart_diagnosis = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])           # We are inclosing input values in two [[[]]] to make the model understand that the model will predict for only one instance.
        
        
        # Showing Result of prediction.
        if(heart_diagnosis[0] == 1):
            heart_diagnosis = 'The person is is having Heart Disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
            
    st.success(heart_diagnosis)       # To display the result.
    






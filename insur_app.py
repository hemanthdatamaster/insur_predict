import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
from sklearn.preprocessing import LabelEncoder

model  = joblib.load('insur.joblib')


def main():
    
    st.title('This is Insurance Cost Prediction App')
    st.text("This is the app that tells you the predicted insurance cost")
    st.sidebar.header('Just fill the information below')
    st.sidebar.text("Regression model is used")
    smoker = st.sidebar.selectbox("Are you a smoker 0 means non smoker 1 means smoker",(0 ,1))
    bmi = st.sidebar.number_input('enter bmi')
    children = st.sidebar.slider('enter no. children', 0, 10, 1)
    sex = st.sidebar.selectbox("select your gender 0 means female 1 means male",(0, 1))

    input  = [[sex,smoker, bmi, children]]
    if st.sidebar.button('predict'):
        prediction  = model.predict(input)
        st.write("Insurance predicted", prediction)
        st.success('Prediction is successfull', icon="✅")
    
        

    



if __name__ == "__main__":
    main()




  
  



     
    
     


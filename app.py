import pickle

import streamlit as st

import numpy as np


df = pickle.load(open('df.pkl','rb'))
m3 = pickle.load(open('m3.pkl','rb'))
rf = pickle.load(open('rf.pkl' , 'rb'))

st.title("Heart Disease Predictor")

age = st.number_input('Age')
sex = st.selectbox('sex(1 = male; 0 = female)', df['sex'].unique() )
cp = st.selectbox('chest pain type', df['cp'].unique() )
trestbps = st.number_input('resting blood pressure( between 94 - 200)')
chol = st.number_input('serum cholestoral ( between 126 - 564)')
fbs	= st.selectbox('fasting blood sugar(1 = true; 0 = fasle)', df['fbs'].unique() )
restecg = st.selectbox('resting electrocardiographic', df['restecg'].unique() )
thalach = st.number_input('maximum heart rate( between 71 - 202)')
exang = st.selectbox('exercise induced angina(1 = yes; 0 = no)', df['exang'].unique() )
oldpeak = st.number_input('ST depression between 0.0-6.0')
slope = st.selectbox(' slope of the peak exercise ST segment', df['slope'].unique() )
ca = st.selectbox(' number of major vessels (0-3) colored by flourosopy', df['ca'].unique() )
thal = st.selectbox(' 1 = normal; 2 = fixed defect; 3 = reversable defect', df['thal'].unique() )

query = np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
query = query.reshape(1,13)

if st.button("Predict"):
    predict=rf.predict(query)
    if predict==1:
        st.write("Petient has Heart Disease")
    else:
        st.write("Petient has no Heart Disease")

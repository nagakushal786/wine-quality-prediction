import streamlit as st
import pickle
import numpy as np

st.title('Wine Quality Prediction')
model=pickle.load(open('model.pkl', 'rb'))

col1, col2, col3=st.columns(3)
with col1:
    fixed_acidity=st.text_input('Fixed Acidity')
with col2:
    volatile_acidity=st.text_input('Volatile Acidity')
with col3:
    citric_acid=st.text_input('Citric Acid')

col4, col5, col6=st.columns(3)
with col4:
    residual_sugar=st.text_input('Residual Sugar')
with col5:
    chlorides=st.text_input('Chlorides')
with col6:
    free_sulphur_dioxide=st.text_input('Free Sulphur Dioxide')

col7, col8, col9=st.columns(3)
with col7:
    tot_sulphur_dioxide=st.text_input('Total Sulphur Dioxide')
with col8:
    density=st.text_input('Density')
with col9:
    pH=st.text_input('pH')

col10, col11=st.columns(2)
with col10:
    sulphates=st.text_input('Sulphates')
with col11:
    alcohol=st.text_input('Alcohol')

if st.button('Predict Quality'):
    input_data=(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulphur_dioxide, tot_sulphur_dioxide, density, pH, sulphates, alcohol)
    np_input_data=np.asarray(input_data)
    np_reshaped_data=np_input_data.reshape(1, -1)
    result=model.predict(np_reshaped_data)[0]

    if result==1:
        st.success('Good Quality Wine')
    else:
        st.error('Bad Quality Wine')
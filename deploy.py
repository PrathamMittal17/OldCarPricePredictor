import pickle
import numpy as np
import pandas as pd
import streamlit as st
from datetime import date

model = pickle.load(open("model.pkl", "rb"))
le = pickle.load(open("le.pkl", "rb"))

df = pd.read_csv("CleanedData.csv")
columns = df.columns[df.columns != 'Price']


def predict():
    testdata = [[
        Location,
        Year,
        np.sqrt(Kilometers_Driven),
        Fuel_Type,
        Transmission,
        Owner_Type,
        Mileage,
        Power,
        Seats,
        Brand,
        le.transform([Model]),

    ]]
    y = model.predict(pd.DataFrame(columns=columns, data=testdata))
    return np.exp(y[0])


st.title("Old Car Price Prediction")
Brand = st.selectbox('Brand', df['Brand'].unique())
Model = st.selectbox('Model', df['Model'][df.Brand == Brand].unique())
Year = st.slider('Year', 1990, date.today().year - 1)
Seats = st.slider('Seats', 2, 8)
Kilometers_Driven = st.number_input('Kilometers Driven', value=0, step=100)
Fuel_Type = st.selectbox('Fuel Type', df['Fuel_Type'].unique())
Transmission = st.selectbox('Transmission', df['Transmission'].unique())
Owner_Type = st.selectbox('Owner Type', df['Owner_Type'].unique())
Mileage = st.number_input('Mileage')
Power = st.number_input('Power')
Location = st.selectbox('Location', df['Location'].unique())
clicked = st.button("Predict Price")

if clicked:
    price = predict()
    price = str(round(price, 2)) + " Lakhs"
    st.header(price)

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

import pickle
html_temp = """
<div style="border:1px;padding:1.5px">
<h1 style="color:black;text-align:center;">Car Price Prediction Streamlit Cloud App</h1>
</div><br>"""
st.markdown(html_temp, unsafe_allow_html=True)

st.write("\n\n"*2)

filename = 'final_model'
model = pickle.load(open(filename, 'rb'))

with st.sidebar:
    st.subheader('Car Specs to Predict Price')

make_model = st.sidebar.selectbox("Model Selection", ("Audi A3", "Audi A1", "Opel Insignia", "Opel Astra", "Opel Corsa", "Renault Clio", "Renault Espace"))
hp_kW = st.sidebar.slider("Horse Power:",min_value=40, max_value=294, value=120, step=5)
age = st.sidebar.selectbox("Age", (0, 1, 2, 3))
km = st.sidebar.number_input("km:",min_value=0, max_value=317000, value=10000, step=5000)
Gears = st.sidebar.number_input("Gears:",min_value=5, max_value=8, value=5, step=1)  
Gearing_Type = st.sidebar.radio("Gearing Type", ("Manual", "Automatic", "Semi-automatic"))


my_dict = {"make_model":make_model, "hp_kW":hp_kW, "age":age, "km":km, "Gears":Gears, "Gearing_Type":Gearing_Type}
df = pd.DataFrame.from_dict([my_dict])

cols = {
    "make_model": "Car Model",
    "hp_kW": "Horse Power",
    "age": "Age",
    "km": "km Traveled",
    "Gears": "Gears",
    "Gearing_Type": "Gearing Type"
}

df_show = df.copy()
df_show.rename(columns = cols, inplace = True)
st.markdown("### Your Car Configuration: \n")
st.table(df_show)

if st.button("Predict"):
    pred = model.predict(df)
    st.success(f"The estimated value of your car price is: {pred[0].astype(int)}$")

import streamlit as st
import pandas as pd
import numpy as np
import pickle
def load_model():
    with open('NEO.pkl','rb') as file:
        model = pickle.load(file)
    return model

model = load_model()
min_value = 0.0001
max_value = 1.0000
st.title("NEO Earth CLose Approaches")
a = st.sidebar.number_input('CA DistanceNominal (au)', format="%.5f"  )
b = st.sidebar.number_input('CA DistanceMinimum (au)',format="%.5f"  )
c = st.sidebar.number_input('V relative(km/s)', min_value = 0.1, max_value = 100.0)
d = st.sidebar.number_input('V infinity(km/s)')
e = st.sidebar.number_input('H(mag)')
input_data = np.array([a,b,c,d,e]).reshape(1,-1)

if st.button('Predict'):
    result = model.predict(input_data)
    st.write(f"Rarity of Earth Close approach is {result}")

			
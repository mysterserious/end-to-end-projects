import streamlit as st
import pickle
import numpy as np
import pandas as pd
from PIL import Image
img=Image.open('moore-house-woods-and-dangaran-mid-century-renovations-architecture-los-angeles-usa-hero-852x479.jpg')
st.image(img)
st.title('House Price Prediction')
model=pickle.load(open('model.pkl','rb'))
sqft_lot=st.slider('Choose Lot Size (in sqft)',520,1651360,5000)
sqft_living=st.slider('Choose Living Area Size (in sqft)',399,5790,1540)
age=st.slider('Choose House Age',0,115,9)
zipcode_dict=pickle.load(open('zipcode_dict.pkl','rb'))
zipcode=st.selectbox('Select Zip Code',list(zipcode_dict.keys()))
zipcode_value=zipcode_dict[zipcode]
bathrooms=st.slider('Choose Number of Bathrooms required',0,8)
bedrooms=st.slider('Choose Number of Bedrooms',0,33)
renov_age=st.slider('Number of years passed after last Renovation',0,99)
sqft_basement=st.slider('Choose Size of Basement (in sqft)',0,4820)
grade=st.slider('Choose House Grade (higher means better house quality)',1,13)
but=st.button('Predict Price')
if but==True:
    final_features=pd.DataFrame(data=[np.array([sqft_lot,sqft_living,age,zipcode_value,bathrooms,bedrooms,renov_age,sqft_basement,grade])],columns=['sqft_lot', 'sqft_living15', 'age', 'zipcode', 'bathrooms', 'bedrooms', 'renov_age', 'sqft_basement', 'grade'])
    price=model.predict(final_features)
    st.subheader('Predicted Price : $'+str(np.round(price[0],2)))
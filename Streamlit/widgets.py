import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name= st.text_input("Enter your name")


age= st.slider("select your age:",0,100,25)

options=["python", "C", "C++", "Java"]
choice= st.selectbox("Choose your favorite language:", options)

st.write(f"You selected {choice}")

st.write(f"Your age is {age}.")

if name:
    st.write(f"Hello, {name}")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df= pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


uploaded_file= st.file_uploader("choose a CSV file", type= 'csv')

if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    st.write(df)
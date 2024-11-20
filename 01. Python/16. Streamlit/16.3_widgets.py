import streamlit as st
import pandas as pd
## Setting the title
st.title("Streamlit Text Input")

name = st.text_input("Enter your Name: ")

age = st.slider("Select Your Age:",0,100,25)
options = ["Python","Java","C++","JavaScript"]
choice = st.selectbox("Choose your favourite programming Language: ",options)
st.write(f"You Selected: {choice}")

if name:
    st.write(f"Hello, {name}\nYour Age is {age}")

upoaded_file = st.file_uploader("Choose a CSV file",type="csv")
if upoaded_file is not None:
    df = pd.read_csv(upoaded_file)
    st.write(df)
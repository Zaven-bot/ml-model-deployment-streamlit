# Title: Testing Streamlit
# Author: Ian Unebasami
# Purpose: Test Streamlit functionality
# Run: streamlit run streamlit_tests.py


# Run: streamlit run 1-streamlit_introduction.py

import streamlit as st
import time
from PIL import Image

st.title("Project: Machine Learning Model Deployment")

# header
st.header("Introduction: This is heading")

# subheading
st.subheader("This is subheader")

# text data
st.text("This is text")
st.text("With this project, I show that I'm capable of implementing a CI/CD Machine Learning pipeline. With a strong portfolio of supervised machine learning models, I wanted to understand how I could deploy those models for myself to use. This curiosity led to be learn technologies such as Docker / FastAPI / AWS / Streamlit so I could deploy an adapatable model capable of receiving input.")

# read input from the user
input_text = st.text_area("Sentiment Input", "type here...")
st.markdown(f"**Your input was:** _{input_text}_")

# Button
button = st.button("Run Model")
if button:
    # st.text("I am clicked!") # ref rexr
    # st.info("Model is running...") # blue
    st.toast("Model is running...")
    # st.warning("Warning") # yellow
    # st.error("Error") # red
    st.image(Image.open("ghibliml.jpg"), width = 400)

# Image
# st.image("https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg?cs=srgb&dl=pexels-anjana-c-169994-674010.jpg", width=100)

# img = Image.open("kgptalkie.png")s
# st.image(img, width=100)

# check box
flag = st.checkbox("Select me")
st.write(flag)
if flag:
    img = Image.open("kgptalkie.png")
    st.image(img, width=100)

# radio button
# st.write(selection)

# select box
# selection = st.selectbox("Choose your model selectbox", ["NLP", "Image", "Audio"])
# st.write(selection)

# multi select
# selection = st.multiselect("Choose your model multiselect", ["NLP", "Image", "Audio"])
# st.write(selection)


with st.spinner("Downloading... Please wait!"):
    st.write("download your model here")
    time.sleep(10)
    
# select numerical value from the given list
# TH = 0.5, large TH -> high precision, small TH -> high recall
st.slider("Set ROC AUC Threshold", 0, 100, step=10)

## ML Model Deployment at Streamlit Server
# Full Streamlit Code Repository: https://github.com/laxmimerit/streamlit-tutorials

# streamlit run 2-app.py

import streamlit as st
import os
import torch
from transformers import pipeline
import boto3

bucket_name = "mlops-huggingface"
local_path = 'tinybert-sentiment-analysis'
s3_prefix = 'ml-models/tinybert-sentiment-analysis-test/'

s3 = boto3.client('s3')
def download_dir(local_path, s3_prefix):
    os.makedirs(local_path, exist_ok=True)
    paginator = s3.get_paginator('list_objects_v2')
    for result in paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix):
        if 'Contents' in result:
            for key in result['Contents']:
                s3_key = key['Key']
                local_file = os.path.join(local_path, os.path.relpath(s3_key, s3_prefix))
                os.makedirs(os.path.dirname(local_file), exist_ok=True)
                s3.download_file(bucket_name, s3_key, local_file)


st.markdown(
    """
    <style>
    .main {
        background-color: #f4e1d2; /* Warm beige background */
        color: #3e2723; /* Deep brown text */
        font-family: 'Lora', serif;
    }
    .stButton>button {
        background-color: #d2691e; /* Terracotta button */
        color: white;
    }
    .stTextArea textarea {
        background-color: #fffaf0; /* Floral white text area */
        color: #3e2723;
    }
    h1, h2, h3, h4, h5, h6, p, div, span, li, a {
        color: #3e2723; /* Deep brown text for all elements */
    }

    .centered {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 12vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.title("Project: Machine Learning Model Deployment")
    st.info("This application allows you to deploy and use a TinyBERT model for sentiment analysis.")

    button = st.button("Download Model")
    if button:
        with st.spinner("Downloading... Please wait."):
            download_dir(local_path, s3_prefix)

    text = st.text_area("Enter your text for sentiment analysis", "...")
    predict = st.button("Predict")

    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

    classifier = pipeline('text-classification',model='tinybert-sentiment-analysis', device=device)

    if predict:
        with st.spinner("Predicting..."):
            output = classifier(text)
            st.success(f"Prediction: {output[0]['label']} with {output[0]['score']:.2f} confidence.")

with col2:
    st.markdown("<div class='centered'>", unsafe_allow_html=True)
    st.image("tinybert-sentiment-analysis/ghibliml.jpg", caption="Classification Cat")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #8b4513;'>", unsafe_allow_html=True)

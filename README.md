# ml-model-deployment-streamlit

# Machine Learning Model Deployment: TinyBERT for Sentiment Analysis

## Overview
This project demonstrates how to deploy a machine learning model using Streamlit, focusing on sentiment analysis with the TinyBERT model. The application allows users to download a pre-trained TinyBERT model, input text for sentiment evaluation, and receive predictions with associated confidence scores.

## Features
- Download the TinyBERT sentiment analysis model from an AWS S3 bucket.
- Input text for sentiment analysis.
- Get predictions along with confidence scores.
- A user-friendly interface with a _warm_ aesthetic design.

## Technologies Used
- **Streamlit**: For building the web application interface.
- **Transformers**: For utilizing the TinyBERT model for text classification.
- **Boto3**: For interacting with AWS S3 to download the model files.
- **PyTorch**: As the backend for the model inference.

## Requirements
Make sure to install the necessary Python packages. You can create a virtual environment and install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Zaven-bot/ml-model-deployment-streamlit.git
cd ml-model-deployment-streamlit
```
### 2. Run the streamlit application
```bash
streamlit run app.py
```
### 3. Usage
* Click on the "Download Model" button to fetch the TinyBert Model from the S3 bucket
* Enter text in text area for sentiment analysis
* Click on "Predict" button to see the sentiment prediction along with its confidence score

## Acknowledgments
Special thanks to the developers of Streamlit, Hugging Face Transformers, and Boto3 for their amazing libraries that made this project possible
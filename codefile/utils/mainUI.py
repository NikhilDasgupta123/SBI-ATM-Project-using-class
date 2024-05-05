import streamlit as st
import string
from utils.transformText import transform_text
from config.config import Config

def main():
    st.markdown("""<h1 style='text-align: center;'>Email Spam Detection App</h1>""", unsafe_allow_html=True)
    input_sms = st.text_area("Enter the message")

    if st.button('Predict'):

        # 1. preprocess
        transformed_sms = transform_text(input_sms)
        # 2. vectorize
        vector_input = Config.cv.transform([transformed_sms])
        # 3. predict
        result = Config.model.predict(vector_input)[0]
        # 4. Display
        if result == 1:
            st.markdown("""
        <h4 style='text-align: center;'>Spam</h4>
    """, unsafe_allow_html=True)
        else:
            st.markdown("""
        <h4 style='text-align: center;'>Not Spam</h4>
    """, unsafe_allow_html=True)
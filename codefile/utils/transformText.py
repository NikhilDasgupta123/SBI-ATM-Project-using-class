import nltk
nltk.download('punkt')
nltk.download('stopwords')

import streamlit as st
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

ps = PorterStemmer()
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer=WordNetLemmatizer()

def transform_text(text):
    review=re.sub('[^a-zA-z]',' ',text)
    review=review.lower()
    review=review.split()
    review=[ps.stem(word) for word in review if not word in stopwords.words('english')] # Stemming
    review=' '.join(review)
    print(review)
    print('\n')
    return review
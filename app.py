import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

ps = PorterStemmer()

@st.cache_resource
def load_models():
    with open('vectorizer.pkl', 'rb') as f:
        tfidf = pickle.load(f)
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return tfidf, model

tfidf, model = load_models()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

st.title("Email/SMS Spam Classifier")
input_sms = st.text_area("Enter the SMS or Email")

if st.button("Predict"):
    if input_sms.strip() == "":
        st.warning("Please enter some text!")
    else:
        transform_sms = transform_text(input_sms)
        vector_input = tfidf.transform([transform_sms])
        result = model.predict(vector_input)[0]
        if result == 1:
            st.error("🚨 Spam!")
        else:
            st.success("✅ Not Spam!")

import streamlit as st
import pickle

# Load the trained model
with open('classifier.pkl', 'rb') as pickle_in:
    classifier = pickle.load(pickle_in)

# Prediction function
def prediction(age, wc, htn, dm):
    htn = 0 if htn == 'no' else 1
    dm = 0 if dm == 'no' else 1

    pred = classifier.predict([[age, wc, htn, dm]])
    return '✅ Kidney disease not detected' if pred[0] == 0 else '⚠️ Kidney disease found'

# Streamlit UI
st.title("Chronic Kidney Disease Classifier")

age = st.number_input("Age", min_value=1, max_value=120)
wc = st.number_input("White Blood Cell Count (cells/cumm)", min_value=3000, max_value=18000)
htn = st.selectbox("Hypertension", ['yes', 'no'])
dm = st.selectbox("Diabetes Mellitus", ['yes', 'no'])

if st.button("Predict"):
    result = prediction(age, wc, htn, dm)
    st.success(result)

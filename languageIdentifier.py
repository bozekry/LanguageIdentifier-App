import joblib
import re
import streamlit as st
import webbrowser
classifier=joblib.load('languageIdentifier.pkl')
st.title("Language detection App")
input_test=st.text_input("please,Enter your language here ","Hello my name is Mahmoud.")
button_clicked=st.button("Get Language Name")
if button_clicked:
    st.text(classifier.predict([input_test]))
if st.button("Available languages"):
    st.text(list(classifier.classes_))
st.markdown("##### by Mahmoud Said")    
  

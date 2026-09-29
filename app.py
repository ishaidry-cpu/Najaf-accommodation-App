import streamlit as st
import google.generativeai as genai
import os

# 1. Set up the look of your app
st.title("Najaf-accommodation-App")
st.write("Welcome! Ask the AI a question below.")

# 2. Securely get the API key 
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# 3. Connect to the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. Create the chat interface
user_input = st.text_input("Your message:")
if st.button("Send to AI"):
    if user_input:
        with st.spinner("Thinking..."):
            response = model.generate_content(user_input)
            st.write(response.text)
    else:
        st.warning("Please type a message first.")

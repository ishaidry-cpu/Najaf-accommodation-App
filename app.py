import streamlit as st
import google.generativeai as genai

st.title("Najaf Accommodation AI")

# Ask for the API key directly on the website
api_key = st.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    st.write("Welcome! Ask the AI a question below.")
    user_input = st.text_input("Your message:")
    
    if st.button("Send to AI"):
        if user_input:
            with st.spinner("Thinking..."):
                response = model.generate_content(user_input)
                st.write(response.text)
        else:
            st.warning("Please type a message first.")
else:
    st.info("👆 Please paste your Google API key above to unlock the AI.")

import streamlit as st
import google.generativeai as genai

st.title("Najaf Accommodation AI")
st.write("Welcome! Ask the AI a question below.")

# Get the API key directly
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

user_input = st.text_input("Your message:")
if st.button("Send to AI"):
    if user_input:
        with st.spinner("Thinking..."):
            response = model.generate_content(user_input)
            st.write(response.text)
    else:
        st.warning("Please type a message first.")

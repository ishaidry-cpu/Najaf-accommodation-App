import streamlit as st
import google.generativeai as genai
import os

st.title("Najaf-accommodation-App")

# 1. Ask for the password (hides the typing with dots)
user_password = st.text_input("Enter the password to access:", type="password")

# 2. Check if the password is correct
if user_password == st.secrets["FH_Najaf"]:
    st.success("Access granted!")
    
    # --- THE REST OF YOUR APP GOES INSIDE THIS IF STATEMENT ---
    st.write("Welcome! Ask the AI a question below.")
    
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
            
# 3. If they typed a wrong password, show an error
elif user_password != "":
    st.error("Incorrect password. Try again.")

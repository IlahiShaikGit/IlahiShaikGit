from dotenv import load_dotenv
load_dotenv() #loading all the environment variables

import streamlit as st 
import google.generativeai as genai
import os


genai.configure(api_key="AIzaSyAae1vcGgh0QIh17qIJPzM2AZ82lIN5wtA")
#function to load gemini pro model and get response


model=genai.GenerativeModel("gemini-pro")


def get_gemini_response(input):
    response=model.generate_content(input)
    response.resolve()
    return response.text


st.set_page_config("GEMINI AI TEXT DEMO")
st.header("GEMINI LLM APPLICATION")
input=st.text_input("input:",key="input")
submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(input)
    st.subheader("the response is:")
    st.write(response)
    
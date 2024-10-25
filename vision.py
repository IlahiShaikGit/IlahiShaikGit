from dotenv import load_dotenv
load_dotenv() #loading all the environment variables

import streamlit as st 
import google.generativeai as genai
import os
from PIL import Image


genai.configure(api_key="AIzaSyAae1vcGgh0QIh17qIJPzM2AZ82lIN5wtA")
#function to load gemini pro model and get response


model=genai.GenerativeModel("gemini-1.5-flash")


def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
        response.resolve()
        return response.text
    else:
        response=model.generate_content(image)
        response.resolve()
        return response.text
        

st.set_page_config("GEMINI AI IMAGE DEMO")
st.header("GEMINI LLM APPLICATION")
input=st.text_input("input prompt:",key="input")
image=st.file_uploader("choose an image: ",type=["jpg","jpeg","png"])
img=""
if image is not None:
    img=Image.open(image)
    st.image(img,caption="uploaded_image")
    
    submit=st.button("Tell me about the image")
    if submit:
        response=get_gemini_response(input,img)
        st.subheader("Response: ")
        st.write(response)
    
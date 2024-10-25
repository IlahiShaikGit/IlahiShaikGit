from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyAae1vcGgh0QIh17qIJPzM2AZ82lIN5wtA")

model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_response(input):
    response=model.generate_content(input,stream=True)
    response.resolve()
    return response.text

st.set_page_config("Q&A DEMO")
st.header("Virtual Interview Bot")

if "chat_history" not in st.session_state:
    st.session_state['chat_history']=[]

input=st.text_input("input :",key="input")
# domain=st.text_input("Enter your domain on which you need to be interviewed: ",key="domain")
submit=st.button("ask the question")

if submit and input:
    # response=get_gemini_response("ask some interview questions and let me answer them and evaluate my answer with your response in the domain of "+domain)
    response=get_gemini_response(input)
    st.session_state['chat_history'].append(("you",input))
    st.subheader("the response is: ")
    # for chunk in response:
    st.write(response)
    st.session_state["chat_history"].append(("VIMBBOT",response))
st.subheader("The Chat History is:")
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")

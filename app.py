# Q and A chatbot

from langchain.llms import OpenAI
# from dotenv import load_dotenv
import os

# load_dotenv()

import streamlit as st

## Funtion to load Open AI model and get response

# def get_openai_response(question):
#     llm = OpenAI(openai_api_key =os.getenv("OPEN_API_KEY"), model_name="text-davinci-003", temperature = 0.5)
#     response = llm(question)
#     return response

def get_openai_response(question):
    llm = OpenAI(model_name="text-davinci-003", temperature = 0.5)
    response = llm(question)
    return response
    
## Intialize stramlit app

st.set_page_config(page_title='Q&A Demo')

st.header("Langchain Application")

input = st.text_input("Input: ", key="input")
response= get_openai_response(input)

submit = st.button("Ask the Question")

#if ask button is clicked

if submit:
    st.subheader("Teh response is")
    st.write(response)
    

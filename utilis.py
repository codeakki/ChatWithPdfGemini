from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
#Embeddings for google genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from prompt import prompt_template
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
import streamlit as st
import os
import google.generativeai as genai



# print(prompt_template)
#Read PDF file
def get_pdf_text(pdf_path):
    """
    Extract text from PDF file
    """
    text = ''
    for pdf in pdf_path:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


# Creating Chunks from pdf file 
def get_text_chunk(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=1000)
    chunks=text_splitter.split_text(text)
    return chunks


# Storing chunks into vector store using google genai embeddings
def get_vectore_store(text_chunk):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store=FAISS.from_texts(text_chunk,embedding=embeddings)
    vector_store.save_local("faiss_index")
             


# Get conversational chain
def get_convesational_chain():
    model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.3)
    prompt=PromptTemplate(template=prompt_template,input_variables=["context","question"])
    chain=load_qa_chain(model,chain_type="stuff",prompt=prompt)
    return chain
    

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    print("HERE")
    new_db = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_convesational_chain()

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    print(response)
    st.write("Reply: ", response["output_text"])
import streamlit as st
import os
import google.generativeai as genai
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from utilis import user_input, get_pdf_text, get_text_chunk, get_vectore_store, get_convesational_chain



load_dotenv()



genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))




def main():
   st.set_page_config(page_title="Chat with multiple PDF", page_icon="🧠", layout="wide")
   st.header("Chat with multiple PDF Using Gemini")

   user_qestion = st.text_input("Ask a Question from the PDF files")

   if user_qestion:
      user_input(user_qestion)  

   with st.sidebar:
      st.title("Upload PDF files")
      pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)

      if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunk(raw_text)
                get_vectore_store(text_chunks)
                st.success("Done")

if __name__ == "__main__":
    main()
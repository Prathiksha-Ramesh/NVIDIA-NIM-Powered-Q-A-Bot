import streamlit as st
import os
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings,ChatNVIDIA
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()

#load the api
os.environ['NVIDIA_API_KEY']=os.getenv('NVIDIA_API_KEY')
llm=ChatNVIDIA(model_name='meta/llama-3.1-8b-instruct')

def vector_embeddings():
    if 'vectors' not in st.session_state:
        st.session_state.embeddings=NVIDIAEmbeddings()
        st.session_state.loader=PyPDFDirectoryLoader('./pdf')
        st.session_state.docs=st.session_state.loader.load()
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=700,chunk_overlap=50)
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs[:30])
        st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)

st.title('NVIDIA NIM Powered Q&A Bot ')  

prompt=ChatPromptTemplate.from_template(
    """
Answer the questions based on the provided context only.
Please provide the most accurate response based on the 
question
<context>
{context}
<context>
Questions:{input}

"""
)

prompt1=st.text_input('enter your questions from documents')
if st.button('Document Embedding'):
    vector_embeddings()
    st.write('FAISS Vector store DB is ready using NVIDIA Embedding')
import time
if prompt1:
    document_chain=create_stuff_documents_chain(llm,prompt)
    retriever=st.session_state.vectors.as_retriever()
    retrieval_chain=create_retrieval_chain(retriever,document_chain)
    response=retrieval_chain.invoke({'input':prompt1})
    start=time.process_time()
    print('Response time:',time.process_time()-start)
    st.write(response['answer'])

    with st.expander('Document Similarity search'):
        for i,doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write('---------------------')



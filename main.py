# general imports
from constants import *

# streamlit imports
import streamlit as st
from utils import *
from streamlit_lottie import st_lottie

# llama index imports
import openai
from llama_index import (
    VectorStoreIndex,
    download_loader,
    ServiceContext,
    set_global_service_context,
)
from llama_index.llms import OpenAI
from llama_index.embeddings import LangchainEmbedding
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

openai.api_key = OpenAI_key  # from constants.py

system_prompt = """
[INST] <>
You are a helpful bank loan officer. You are going to be given a bank statement
to analyse and you must provide accurate insights about its contents.

If a question doesn't make any sense, or is not factually coherent, explain what is wrong with
the question instead of answering something incorrect. If you don't know the answer, don't share
inaccurate information. 

Your goal is to provide insightful answers about the financial background of an individual.
<>
"""
llm = OpenAI(model="gpt-4-1106-preview", system_prompt=system_prompt)

embeddings = LangchainEmbedding(HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"))

service_context = ServiceContext.from_defaults(llm=llm, embed_model=embeddings)
set_global_service_context(service_context)

# import lottie
lottie_file = load_lottieurl()  # animation url

st.set_page_config(page_title="loan_gpt")
st_lottie(lottie_file, height=175, quality="medium")

st.title("**Loan Check: Business Loan Analysis**")

if "uploaded" not in st.session_state:
    st.session_state["uploaded"] = False
    st.session_state["filename"] = None
    st.session_state["initial_response"] = None

if "query_engine" not in st.session_state:
    st.session_state["query_engine"] = None


def reset():
    st.session_state["uploaded"] = False
    st.session_state["filename"] = None
    st.session_state["initial_response"] = None
    st.session_state["query_engine"] = None


if not st.session_state["uploaded"]:
    st.write("Upload a bank statement and analyze loan worthiness.")
    input_file = st.file_uploader("Choose a file")

    if input_file and does_file_have_pdf_extension(input_file):
        path = store_pdf_file(input_file, dir)  # default dir is ./statements/
        scs = st.success("File successfully uploaded")
        filename = input_file.name

        with st.spinner("Analyzing document..."):
            PyMuPDFReader = download_loader("PyMuPDFReader")
            loader = PyMuPDFReader()
            documents = loader.load(file_path=path, metadata=True)
            index = VectorStoreIndex.from_documents(documents)
            query_engine = index.as_query_engine()
            st.session_state["query_engine"] = query_engine
        scs.empty()

        st.session_state["uploaded"] = True
        st.session_state["filename"] = filename

        st.rerun()

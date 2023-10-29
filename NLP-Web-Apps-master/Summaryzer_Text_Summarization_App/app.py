# Import necessary libraries
from __future__ import unicode_literals
import streamlit as st
from spacy_summarization import text_summarizer, nlp
from gensim.summarization import summarize
from nltk_summarization import nltk_summarizer
import time
import spacy
from bs4 import BeautifulSoup
import urllib.request
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# Define a Streamlit app
def main():
    st.title("Text Summarization App")
    option = st.selectbox("Choose an option:", ["Home", "Text Analysis", "URL Analysis", "Compare Summarizers", "About"])

    if option == "Home":
        st.header("Welcome to the Text Summarization App")
        st.write("This app provides text summarization using various algorithms.")

    elif option == "Text Analysis":
        st.header("Text Analysis")
        rawtext = st.text_area("Enter the text you want to summarize:")
        if st.button("Summarize"):
            st.write("Original Text:")
            st.write(rawtext)
            final_summary = text_summarizer(rawtext)
            st.write("Summary:")
            st.write(final_summary)

    elif option == "URL Analysis":
        st.header("URL Analysis")
        raw_url = st.text_input("Enter the URL of the page you want to summarize:")
        if st.button("Get Text and Summarize"):
            rawtext = get_text(raw_url)
            st.write("Original Text:")
            st.write(rawtext)
            final_summary = text_summarizer(rawtext)
            st.write("Summary:")
            st.write(final_summary)

    elif option == "Compare Summarizers":
        st.header("Compare Summarizers")
        rawtext = st.text_area("Enter the text you want to summarize:")
        if st.button("Compare Summarizers"):
            st.write("Original Text:")
            st.write(rawtext)
            final_summary_spacy = text_summarizer(rawtext)
            st.write("Spacy Summary:")
            st.write(final_summary_spacy)
            final_summary_gensim = summarize(rawtext)
            st.write("Gensim Summary:")
            st.write(final_summary_gensim)
            final_summary_nltk = nltk_summarizer(rawtext)
            st.write("NLTK Summary:")
            st.write(final_summary_nltk)
            final_summary_sumy = sumy_summary(rawtext)
            st.write("Sumy Summary:")
            st.write(final_summary_sumy)

    elif option == "About":
        st.header("About")
        st.write("This is a Streamlit-based Text Summarization App.")
        st.write("It allows you to summarize text using various algorithms.")

# Define the main entry point
if __name__ == "__main__":
    main()

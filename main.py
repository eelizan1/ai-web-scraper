import streamlit as st
from scrape import scrape_website

# Streamlit UI
st.title("AI Web Scraper")
url = st.text_input("Enter Website URL: ")

if st.button("Scrape Site"): 
    st.write("Scraping the website") 
    result = scrape_website(url)
    print(result)
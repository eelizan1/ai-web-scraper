import streamlit as st

# Streamlit UI
st.title("AI Web Scraper")
url = st.text_input("Enter Website URL: ")

if st.button("Scrape Site"): 
    st.write("Scraping the website") 
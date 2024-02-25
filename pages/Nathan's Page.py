import streamlit as st
import streamlit.components.v1 as components
from bs4 import BeautifulSoup
import requests, json, lxml
import pandas as pd

st.set_page_config(layout='wide')


st.header("The War in Ukraine")
components.iframe("https://liveuamap.com", 1250, 600)

headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

# https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls
params = {
  'q': 'ukraine war news',  # query
  'gl': 'uk',    # country to search from
  'hl': 'en'     # language
}

# https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts
html = requests.get("https://www.google.com/search", headers=headers, params=params, timeout=300)
soup = BeautifulSoup(html.text, 'lxml')

def extract_results(soup):
    main = soup.select_one("#main")

    res = []
    for gdiv in main.select('.g, .fP1Qef'):
        res.append(extract_section(gdiv))
    return res

def extract_section(gdiv):
    # Getting our elements
    title = gdiv.select_one('h3')
    link = gdiv.select_one('a')
    description = gdiv.find('div', class_='kb0PBd cvP2Ce')
    return {
        # Extract title's text only if text is found
        'title': title.text if title else None,

        'link': link['href'] if link else None,
        'description': description.text if description else None
    }

results = extract_results(soup)

st.subheader("Breaking News")

for website in results:
    st.write(f"""**%(title)s**, %(link)s\n
    %(description)s""" % website)

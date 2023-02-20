import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import requests
import json
import time


st.set_page_config(layout="wide")

image = Image.open('images/Logo.jpeg')

st.image(image, width = 500)

st.title('Crypto Price App')

st.markdown("""
            This app retrieves Crypto rates!!
            ***
            """)

expander_bar = st.expander("About")

expander_bar.markdown("""
                      * **Python Libraries:** Streamlit, Image, pandas, base64, matplotlib.pyplot, seaborn, BeautifulSoup, requests, json, Time.
                      * **Data Source:** [CoinMarketCap](https://wikipedia.org/)
                      * **Credit:** Web Scrapper adapted from the Medium article *[Web scrapping Crypto prices with Python](https://wikipedia.com/)
                      """)

# Page layout:
col1 = st.sidebar
col2, col3 = st.columns((2,1)) #Width of data frame column should be twice the size of the bar chart column

col1.header('Input Options')

currency_price_unit = col1.selectbox('Select currency for price')



"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd


st.header("Instructional Items")
st.subheader("Item 1")
st.write("""Objectives: The linked webpage is the official documentation of Streamlit. There are various web pages within the home page, which include “Installation”, “Fundamentals”, “Tutorials”, and “Use GitHub Codespaces”. After installing Streamlit, the user is directed to the “Main Concepts'' section under “Fundamentals”. The “Main Concepts” cover a variety of topics, including running the script, data flow, styling data, drawing charts/maps, taking in user input, and more. If the user finishes this section, they are welcome to start the “Advanced Concepts” section, which has more features. These lessons describe the given features, give examples of the feature being used, and are open-ended such that a user following along can make their own examples. 
\nEngagement: The time for this can vary greatly from user to user, as they are free to follow their own pace while reading the examples and making their own examples. However, I found that I was able to get through the “Installation” and “Main Concepts” sections in roughly an hour. It is worth noting that I have a high amount of experience with Python, so I was faster than the average new user. 
\nURL: https://docs.streamlit.io/get-started 
""")

st.subheader("Item 2")
st.write("""Objectives: This YouTube video is a full course that walks viewers through building 12 different data science apps using Python and Streamlit. 
\nEngagement: The entire video linked below is more than three hours. However, it is clearly divided into different sections so that viewers can select different tutorials that they are most interested in.
\nURL: https://www.youtube.com/watch?v=JwSS70SZdyM
""")

st.subheader("Item 3")
st.write("""Objectives: This YouTube video is a presentation on how Streamlit can be used to create an interactive dashboard app. The video first starts with defining what should be included in a dashboard app. Next, the video explains how and why Streamlit can be used for this task. The rest of the video is used to show off an example app and walk through the background programming that allows it to function.
\nEngagement: The video is 30 minutes long. However, the video has a natural progression and provides meaningful examples to make the content more engaging. The video provides a good starting point for beginners while touching on topics for more advanced users.
\nhttps://www.youtube.com/watch?v=asFqpMDSPdM
""")

st.image("gif.gif")
st.image("gif2.gif")
st.image("gif3.gif")
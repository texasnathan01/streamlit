import streamlit as st
import pandas as pd

st.write("""
# Howdy! Welcome to our streamlit application
""")

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
\nURL: https://www.youtube.com/watch?v=asFqpMDSPdM
""")

st.subheader("Item 4")
st.write("""Objectives: This YouTube video covers the development of a progress bar. This topic covers several key components of a Streamlit page including GUI, interactable content, saving data, and using user inputs. While this is a basic example, the concepts presented can be applied in a variety of different instances. For example, a progress bar on a simulation or task currently being run would be very useful.
\nEngagement: The video is approximately 20 minutes long. This video dissects the individual steps required to create the progress bar. These steps are explained in a simple and succinct manner that allows the viewer to code alongside the guide. Additionally, the results of most of the individual changes are then shown so the viewer can see how the changes impact the website. 
\nURL: https://www.youtube.com/watch?v=dPYlqTGA6wc&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=11
""")

st.subheader("Item 5")
st.write("""Objectives: This video covers the usage of the sidebar of Streamlit websites and about how to incorporate graphics into your site. The video first covers adding a sidebar as well as some buttons that the user can interact with. The video then show how to use the user inputs to influence a graph that is then depicted. This video is intended to demonstrate some of the basic features that you can use in Streamlit.
\nEngagement: This video is approximately 15 minutes. The video breaks down the process of adding these two components and presents a side-by-side view of the code and resulting output. Similar to the video covering the progress bar, this video provides viewers with the option to code alongside the video.
\nURL: https://www.youtube.com/watch?v=cUKqsnLGQBw&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=14
""")

st.subheader("Item 6")
st.write("""Objectives: This YouTube tutorial is built around practical applications to level up your base streamlit skills. The video starts off by explaining a series of tips and tricks to users already familiar with the platform. Overall, the video is targeted at people with intermediate to advanced exposure to streamlit. A wide overview of base components is included in this tutorial but the creator specifically focuses on tools most important for the project at hand. An example of this would be an exploration of text highlighting, annotating, and customization. The sections detail linear flow actions needed for dropdown menus and adaptive displays with conditionals. Google Sheet automation and integration with Google Forms are then covered as the instructor Avra teaches you how to build an interactive survey platform. Finally, database integration is explored as Avra teaches you how to store, and present user-uploaded information on the site all within one Python script.
\nEngagement: This video is 1 hour and 23 minutes long and is edited in the popular “code-along-with-me” style on YouTube. The first 40 minutes of the video is more akin to a lecture about features and testing individual components Avra is highlighting. This section can be done with the initial pacing of the video. The last 40 minutes focus on building a specific web application, Although, Avra provides pseudocode in his description this section should take an hour and a half to follow along with because the user was encouraged to stop the video to find their own solutions.
\nURL: https://www.youtube.com/watch?v=0gT_Ro8ijII&t=337s
""")

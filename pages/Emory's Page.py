import folium
import streamlit as st
import pandas as pd
from streamlit_folium import st_folium

st.markdown("<h1 style='text-align: center'>BigFoot Sightings in Texas</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center'>Click on green icons to learn more</p>", unsafe_allow_html=True)

# get data
df = pd.read_csv('https://query.data.world/s/5jillup67kpdqxcke4l74gxcwasc3a?dws=00000')
df = df.dropna(subset=['latitude', 'longitude'])
df = df[(df["state"] == "Texas")]

# create map
m = folium.Map(location=[df["latitude"][4], df["longitude"][4]], zoom_start=7)

# add map markers
for index, row in df.iterrows():
    latitude = row["latitude"] 
    longitude = row["longitude"]
    if (pd.notna(latitude) and pd.notna(longitude)):
        folium.Marker(
            location = [row["latitude"], row["longitude"]],
            icon=folium.Icon(color="green")
        ).add_to(m)


output = st_folium(
    m, width=1000, height=700, returned_objects=["last_object_clicked"]
)

# display observation data for last clicked marker
if (output["last_object_clicked"]):
    lat = output["last_object_clicked"]["lat"]
    lng = output["last_object_clicked"]["lng"]
    observation = df[(df["latitude"] == lat) & (df["longitude"] == lng)]
    st.write(observation["title"].values[0])
    st.write(observation["observed"].values[0])
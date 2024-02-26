import cv2
import streamlit as st
import numpy as np
from skimage.filters import sobel
from skimage.transform import swirl
from skimage.color import rgb2gray
from PIL import Image

def get_video(swirl_strength, threshold, edge):

    while cap.isOpened() and not stop_button_pressed:

        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if sobel_pressed:
             
            if edge == "Basic Edge :movie_camera:":
                frame = rgb2gray(frame)
                frame = np.round((1 - np.array(sobel(frame)))*255).astype(np.uint8)
            
            elif edge == "***Evil Edge***":
                frame = np.round((np.array(sobel(frame)))*255).astype(np.uint8)
            
            else:
                frame = np.round((1 - np.array(sobel(frame)))*255).astype(np.uint8)
                
            min=np.min(frame)
            max=np.max(frame)

            LUT=np.zeros(256,dtype=np.uint8)
            LUT[min:max+1]=np.linspace(start=0,stop=255,num=(max-min)+1,endpoint=True,dtype=np.uint8)
            frame = Image.fromarray(LUT[frame])

        if swirl_pressed:
            frame = swirl(frame, rotation=0, strength=2, radius=swirl_strength)


        if grey_pressed:
            frame = rgb2gray(frame)
            if threshold:
                frame = np.round((1 - np.array(frame))*255).astype(np.uint8)

        frame_placeholder.image(frame, channels="RGB")

frame_placeholder = st.empty()
frame_placeholder.image("Crazy Camera Landing.png", channels="RGB")

st.title("Crazy Video Camera App Options")
st.write("")

col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])

with col1:
    start_button_pressed = st.button("Normal")

with col2:
    sobel_pressed = st.button("Edgey")
    edge = st.radio("",["Basic Edge :movie_camera:","***Evil Edge***", ":rainbow[Color Edge]"])
    
with col3:
    grey_pressed = st.button("Gray")
    st.write("")
    threshold = st.toggle("Invert")

with col4:
    swirl_pressed = st.button("Swirl")
    st.write("")
    swirl_strength = st.select_slider("Strength of Swirl",
                                      options=[100, 200, 300, 400, 500])

with col5:
    stop_button_pressed = st.button("Stop")


if start_button_pressed | sobel_pressed | grey_pressed | swirl_pressed:
    cap = cv2.VideoCapture(0)
    get_video(swirl_strength, threshold, edge)

if stop_button_pressed:
    st.text("The video has stopped")
    frame_placeholder.image("Crazy Camera Landing.png", channels="RGB")

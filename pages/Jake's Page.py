import cv2
import streamlit as st
import numpy as np
from skimage.filters import sobel
from skimage.transform import swirl
from skimage.color import rgb2gray
from PIL import Image

def get_video():

    while cap.isOpened() and not stop_button_pressed:
    
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        if sobel_pressed:
            frame = np.round((1 - np.array(sobel(frame)))*255).astype(np.uint8)
            min=np.min(frame)
            max=np.max(frame)

            LUT=np.zeros(256,dtype=np.uint8)
            LUT[min:max+1]=np.linspace(start=0,stop=255,num=(max-min)+1,endpoint=True,dtype=np.uint8)
            frame = Image.fromarray(LUT[frame])
        
        if swirl_pressed:
            frame = swirl(frame, rotation=0, strength=10, radius=120)
            
    
        if grey_pressed:
            frame = rgb2gray(frame)

        frame_placeholder.image(frame, channels="RGB")

frame_placeholder = st.image("Crazy Camera Landing.png")

st.title("Crazy Video Camera App")
start_button_pressed = st.button("Start")
sobel_pressed = st.button("Edgey")
grey_pressed = st.button("Grey")
swirl_pressed = st.button("Swirl")
stop_button_pressed = st.button("Stop")

if start_button_pressed | sobel_pressed | grey_pressed | swirl_pressed:
    cap = cv2.VideoCapture(0)
    frame_placeholder = st.empty()
    get_video()

if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
    st.text("The video has stopped")
    frame_placeholder.image("Crazy Camera Landing.png", channels="RGB")

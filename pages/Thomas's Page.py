import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title='Can it run Doom?', page_icon="./Images/DoomIcon.png")

doom_string = """
   <head>
     <meta charset="utf-8">
     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
     <title>DOOM</title>
     <style type="text/css">
       .dosbox-container { width: 640px; height: 400px;}
     </style>
   </head>
   <body>
     <div id="dosbox"></div>
     <br/>
     <button onclick="dosbox.requestFullScreen();">Make fullscreen</button>
    
     <script type="text/javascript" src="https://js-dos.com/cdn/js-dos-api.js"></script>
     <script type="text/javascript">
       var dosbox = new Dosbox({
         id: "dosbox",
         onload: function (dosbox) {
           dosbox.run("https://js-dos.com/cdn/upload/DOOM-@evilution.zip", "./DOOM/DOOM.EXE");
         },
         onrun: function (dosbox, app) {
           console.log("App '" + app + "' is runned");
         }
       });
     </script>
   </body>
"""

st.markdown("<h1 style='text-align: center; color: black;'>Can it run <font color=red>DOOM</font>?</h1>", unsafe_allow_html=True)

html(doom_string, width=640, height=400)


st.markdown("""
    <h3 id="controls">Controls:</h3>
    <ul>
        <li>Move: UP, DOWN, LEFT, RIGHT</li>
        <li>Use: W</li>
        <li>Fire: S</li>
        <li>Speed on: SPACE</li>
        <li>Strafe on: ALT</li>
        <li>Strafe: A, D</li>
        <li>Menu Select: Enter</li>
    </ul>
""", unsafe_allow_html=True)

st.markdown('<p></p><p style="text-align: left">"It Runs Doom" is an expression indicating that a device is capable of running the 1993 first-person shooter video game Doom, which has been successfully ported to a variety of electronic gadgets designed for purposes other than gaming.</p>', unsafe_allow_html=True)

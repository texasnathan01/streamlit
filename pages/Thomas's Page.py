import streamlit as st
from streamlit.components.v1 import html

doom_string = """
 <!doctype html>
 <html lang="en-us">
   <head>
     <meta charset="utf-8">
     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
     <title>DOOM</title>
     <style type="text/css">
       .dosbox-container { width: 320px; height: 200px; }
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
 </html>
"""

html(doom_string, width=640, height=400)
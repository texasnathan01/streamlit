import streamlit as st
from streamlit.components.v1 import html

doom_string = """
   <head>
     <meta charset="utf-8">
     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
     <title>DOOM</title>
     <style type="text/css">
       .dosbox-container { width: 320px; height: 200px; margin: auto;}
       .dosbox-container > .dosbox-overlay { background: url(https://web.archive.org/web/20240219141702/https://js-dos.com/cdn/DOOM.png); }
     </style>
   </head>
   <body>
     <div id="dosbox"></div>
     <br/>
     <button onclick="dosbox.requestFullScreen();">Make fullscreen</button>
     
     <script type="text/javascript" src="https://web.archive.org/web/20240219141703/https://js-dos.com/cdn/js-dos-api.js"></script>
     <style>
         canvas {
             width: 100%;
             height: 100%;
             margin: auto;
             padding: 0;
         }
     </style>
     <script type="text/javascript">
       var dosbox = new Dosbox({
         id: "dosbox",
         onload: function (dosbox) {
           dosbox.run("https://web.archive.org/web/20230924174938/https://js-dos.com/cdn/upload/DOOM-@evilution.zip", "./Doom.exe");
         },
         onrun: function (dosbox, app) {
           console.log("App '" + app + "' is runned");
         }
       });
     </script>
   </body>
"""

"""dosbox.run("./Doom/DOOM-@evilution.zip", "./Doom/DOOM-@evilution/DOOM");"""


#html(doom_string, width=320, height=200)

doom_string_2 = """
<head>
 <meta charset="utf-8">
  <title>Digger js-dos 6.22</title>
  <script src="https://web.archive.org/web/20240112092319/https://js-dos.com/6.22/current/js-dos.js"></script>
  <style>
  canvas {
     width: 640px;
     height: 400px;
   }
 </style>
</head>

<body>
  <canvas id="jsdos"></canvas>
  <script>
   Dos(document.getElementById("jsdos"), { 
      wdosboxUrl: "https://web.archive.org/web/20240121122727/https://js-dos.com/6.22/current/wdosbox.js" 
      }).ready((fs, main) => {
  fs.extract("https://web.archive.org/web/20230924174938/https://js-dos.com/cdn/upload/DOOM-@evilution.zip").then(() => {
     main(["./Doom"])
     });
    });
  </script>
  </body>
"""

doom_string_3 = """"""


#html(doom_string_2, width=640, height=400)


doom_string_4 = """
 <!doctype html>
 <html lang="en-us">
   <head>
     <meta charset="utf-8">
     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
     <title>DOOM</title>
     <style type="text/css">
       .dosbox-container { width: 320px; height: 200px; }
       .dosbox-container > .dosbox-overlay { background: url(https://js-dos.com/cdn/DOOM.png); }
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
           dosbox.run("./Doom/DOOM-@evilution.zip", "C ./DOOM.exe");
         },
         onrun: function (dosbox, app) {
           console.log("App '" + app + "' is runned");
         }
       });
     </script>
   </body>
 </html>
"""


#html(doom_string_4, width=640, height=400)


doom_string_5 = """
 <!doctype html>
   <html lang="en-us">
     <head>
       <meta charset="utf-8">
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
       <title>js-dos api</title>
       <style type="text/css">
         .dosbox-container { width: 640px; height: 400px; }
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
             dosbox.run("https://js-dos.com/cdn/digger.zip", "./DIGGER.COM");
           },
           onrun: function (dosbox, app) {
             console.log("App '" + app + "' is runned");
           }
         });
       </script>
     </body>
   </html>
   """
   
# html(doom_string_5, width=640, height=400)

doom_string_6 = """
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

html(doom_string_6, width=640, height=400)
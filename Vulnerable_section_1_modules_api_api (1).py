 import time
 import datetime
 import uvicorn
 import gradio as gr
 from threading import Lock
 from io import BytesIO
 
 
 def decode_base64_to_image(encoding):
     if encoding.startswith("http://") or encoding.startswith("https://"):
        import requests
         response = requests.get(encoding, timeout=30, headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'})
         try:
             image = Image.open(BytesIO(response.content))
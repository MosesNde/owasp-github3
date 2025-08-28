 import re
 import requests
 from urllib.parse import urlparse
 from bs4 import BeautifulSoup
 
 OLLAMA_URL = 'http://localhost:11434/api/generate'
 
 def duckduckgo_check(domain):
     import requests
     from bs4 import BeautifulSoup
 
 
 def fetch_website_text(url):
     if not url.startswith("http://") and not url.startswith("https://"):
         url = "http://" + url  # Add default scheme if missing
     try:
         response = requests.get(url, timeout=5)
         response.raise_for_status()
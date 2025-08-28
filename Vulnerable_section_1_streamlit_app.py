 import requests
 from yt_dlp import YoutubeDL
 from bs4 import BeautifulSoup
 
 # Google Gemini config
 gemini_api_key = os.environ["GEMINI_API_KEY"]
                 ydl.download(yt_url)
 
         case "Audio file link":
            downloaded_file = requests.get(audio_link)
             with open(AUDIO_FILE_NAME, "wb") as f:
                 f.write(downloaded_file.content)
 
             if len(audio_link.strip()) != 0:
                 if audio_link.startswith("https://castro.fm/episode/"):
                     soup = BeautifulSoup(
                        requests.get(audio_link).content, "html.parser"
                     )
                     audio_link = soup.source.get("src")
                 get_printable_results()
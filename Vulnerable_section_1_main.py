 load_dotenv()
 
 app = Flask(__name__)
configuration = Configuration(os.getenv("CHANNEL_ACCESS_TOKEN"))
 handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))
 
 
     try:
         handler.handle(body, signature)
     except InvalidSignatureError:
         abort(400)
     return 'OK'
 
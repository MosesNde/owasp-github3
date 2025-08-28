 import re
 import html2text
 from flask import json
from config.configuration import MODE
 from modules.user_story_analyzer.config.configuration import PROMPTS
 from dotenv import load_dotenv
 from services.infisical_sdk import get_infisical_secret
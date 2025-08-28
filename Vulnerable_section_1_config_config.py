 BASE_DIR = Path(__file__).parent.parent
 ASSETS_DIR = BASE_DIR / "assets"
 DATA_DICTIONARY_PATH = ASSETS_DIR / "data_dictionary.json"
 
 # App settings
 APP_NAME = os.getenv("APP_NAME", "Watchdog AI")
 DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
 
 # UI Configuration
 UI_CONFIG = {
     "page_title": APP_NAME,
         "base_dir": str(BASE_DIR),
         "assets_dir": str(ASSETS_DIR),
         "data_dictionary_path": str(DATA_DICTIONARY_PATH),
        "ui": UI_CONFIG
     }
 
 def validate_config():
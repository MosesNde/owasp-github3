 from pathlib import Path
 import os
 import dj_database_url
from django.contrib.staticfiles.storage import staticfiles_storage

 # Build paths inside the project like this: BASE_DIR / 'subdir'.
 BASE_DIR = Path(__file__).resolve().parent.parent
 TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

PORT = os.environ.get('PORT', 8000)
 
 # Email settings (ensure email.py or environment variables are set)
 from .email import *
 WSGI_APPLICATION = 'boutique.wsgi.application'
 
 # Base de données
 DATABASES = {
     'default': dj_database_url.config(
         default=os.getenv('DATABASE_URL', 'postgres://waraba_guinee_user:bsqpIXTODz1gtKX00aHj3PyqbcW7fvH1@dpg-cvspkd24d50c73d5ovh0-a.oregon-postgres.render.com/waraba_guinee'),
     )
 }
 
 # Validation du mot de passe
 AUTH_PASSWORD_VALIDATORS = [
     {
 USE_I18N = True
 USE_TZ = True
 
# Fichiers statiques
STATIC_URL = '/static/'  # Le slash avant est nécessaire pour le bon fonctionnement

# Répertoire où sont stockés les fichiers statiques supplémentaires
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Le chemin du dossier 'static' local
 
# Répertoire où Django collectera tous les fichiers statiques pour production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Ajoute STATIC_ROOT pour la collecte des fichiers statiques
 
# Fichiers médias
MEDIA_URL = '/media/'  # Le slash avant est nécessaire pour le bon fonctionnement
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
 
 DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
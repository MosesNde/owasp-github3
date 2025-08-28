     }
 }
 
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'votre_db_name'),
        'USER': os.environ.get('MYSQL_USER', 'votre_db_user'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'votre_db_password'),
        'HOST': os.environ.get('MYSQL_HOST', '127.0.0.1'),
        'PORT': os.environ.get('MYSQL_PORT', '3306'),
         'OPTIONS': {
             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            # Forcez l'utilisation de TCP/IP au lieu du socket local
            'read_default_file': None,
         }
     }
 }
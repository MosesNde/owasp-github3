         'NAME': config('MYSQL_DATABASE'),
         'USER': config('MYSQL_USER'),
         'PASSWORD': config('MYSQL_PASSWORD'),
        'HOST': config('DB_HOST', 'db'),  # Use 'db' as default from .env
         'PORT': config('DB_PORT', '3306'),  # Use '3306' as default from .env
     }
 }
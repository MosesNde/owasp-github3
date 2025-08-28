         'NAME': config('DB_NAME'),              # Use the environment variable for DB name
         'USER': config('DB_USER'),              # Use the environment variable for username
         'PASSWORD': config('DB_PASSWORD'),          # Use the environment variable for password
        'HOST': config('DB_HOST', 'db'),        # Use 'db' as default if not set
         'PORT': config('DB_PORT', '5432'),          # Use '5432' as default for PostgreSQL
     }
 }
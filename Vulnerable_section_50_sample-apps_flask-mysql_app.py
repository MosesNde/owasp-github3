     app.run()
 mysql = MySQL()
 
app.config['MYSQL_DATABASE_HOST'] = 'db'
 app.config['MYSQL_DATABASE_USER'] = 'user'
 app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
 app.config['MYSQL_DATABASE_DB'] = 'db'
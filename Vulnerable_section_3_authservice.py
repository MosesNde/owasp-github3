 from flask import session
 import mariadb
 from accountservice import AccountService
 
 config = {
      'user': 'root',
         print('res is ', res)
         if res:
             session['customer_id'], session['username'] = res[0], res[1]
         
         return session
     
\ No newline at end of file
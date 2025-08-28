         if not re.match(pattern, data['username']):
             raise ValueError('Unable to sign up, please check input data.')
         
        authservice.login(data1['username'], data1['password'])
 
         # make sure only to go to index with session when user is logged in
         if 'username' in session:
         # delete critical user information from session once logged out
         session.pop('customer_id', None)
         session.pop('username', None)
         return redirect(url_for('index', session=session))
     return render_template('logout.html')
     
\ No newline at end of file
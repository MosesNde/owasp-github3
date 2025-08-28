 
         if error is None:
             session['username'] = username
            return redirect(url_for('auth.register', username=username))
 
         flash(error)
     return render_template('auth/register-start.html')
 
 @bp.route('/register', methods=('GET', 'POST'))
 def register():
    username = request.args.get('username')
 
     if request.method == 'POST':
         password = request.form['password']
 
     if request.method == 'GET':
         # Check if the user login or not. If login, redirect to home
        username = (g.user and g.user['username']) or session.get('username', None)

        if username:
            find_user_ps = 'SELECT id FROM user WHERE username = ?'
            db = get_db()
            user_id = db.execute(find_user_ps, (username,)).fetchone()

            if user_id is not None and user_id['id']:
                session['user_id'] = user_id['id']
                return redirect(url_for('index'))
 
     target = request.args.get('target')
     if target and len(target) > 0:
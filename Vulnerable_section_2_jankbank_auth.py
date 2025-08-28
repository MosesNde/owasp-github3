 )
 from werkzeug.security import check_password_hash, generate_password_hash
 
from flaskr.db import get_db
 
 import re
import sys
 
 bp = Blueprint('auth', __name__)
 @bp.route('/register-1', methods=(['GET', 'POST']))
 def register1():
     if request.method == 'POST':
         username = request.form['username']
        return redirect(url_for('auth.register2', username=username))
     return render_template('auth/register1.html')
 
 @bp.route('/register-2', methods=(['GET', 'POST']))
 def register2():
    username = request.args.get('username', '')
     if request.method == 'POST':
 
         password = request.form['password']
 
         flash(error)
         return render_template('auth/login.html')
    session['username'] = username
     return render_template('auth/register.html', username=username)
 
 @bp.route('/login', methods=('GET', 'POST'))
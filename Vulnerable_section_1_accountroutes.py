 account_blueprint = Blueprint('account', __name__)
 
 accservice = AccountService()

# Define a list of trusted domains
trusted_domains = ["localhost", "127.0.0.1"]

# Custom decorator to check if the URL is whitelisted
def whitelist_redirect(func):
    def wrapper(*args, **kwargs):
        url = request.args.get('url')
        if any(domain in url for domain in trusted_domains):
            return func(*args, **kwargs)
        else:
            return redirect('/')
    return wrapper
     
 @account_blueprint.route('/account', methods=['GET', 'POST'])
@whitelist_redirect
 def create_account():
     try:
         if request.method == 'POST':
             data = request.form
 
 @account_blueprint.route('/account/<int:account_id>', methods=['GET'])
 def account(account_id):
     try:
         if request.method == 'GET':
             # Get a single account
             acct = accservice.getAccountById(int(account_id))
 @account_blueprint.route('/account/<int:account_id>/withdraw', methods=['POST'])
 def withdraw(account_id):
     try:
         if request.method == 'POST':
             acct = accservice.getAccountById(int(account_id))
             data = request.form
 @account_blueprint.route('/account/<int:account_id>/deposit', methods=['POST'])
 def deposit(account_id):
     try:
         if request.method == 'POST':
             acct = accservice.getAccountById(int(account_id))
             data = request.form
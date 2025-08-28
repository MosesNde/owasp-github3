 from .forms import UserRegistrationForm, UserLoginForm
 from .models import User
 
 def register_view(request):
     if request.method == 'POST':
         form = UserRegistrationForm(request.POST)
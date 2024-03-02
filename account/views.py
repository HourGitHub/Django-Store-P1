# from base64 import urlsafe_b64encode
# from django.contrib.sites.shortcuts import get_current_site
# from django.shortcuts import redirect, render
# from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes
# from account.tokens import AccountActivationTokenGenerator
# from .tokens import AccountActivationTokenGenerator


# from .forms import RegistrationForm

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

# from orders.views import user_orders

from .forms import RegistrationForm
from .models import UserBase
from .tokens import account_activation_token


@login_required
def dashboard(request):
    return render(request, 
                  'account/user/dashboard.html')


def account_register(request):
  

    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.email = register_form.cleaned_data['email']
            user.set_password(register_form.cleaned_data['password'])
            user.is_active = False
            user.save()

            # Setup email
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)

            # Redirect to a success page or login page
            return redirect('success_registration')

    else:
        register_form = RegistrationForm()

    return render(request, 'account/registration/register.html', {'form': register_form})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.object.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoneNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')





from base.models import *
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from pickle import GET
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from random import randint
from base.models import *
from base.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponse

# from .forms import SetPasswordForm, PasswordChangeForm

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

# from django.urls import reverse
# from base.scripts import save_token
# from django.forms.models import modelformset_factory

""" PASSWORD RESET"""

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)

		if password_reset_form.is_valid():                                
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))

			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "new_telegram_bot_service/password-reset-email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
		return redirect ("password_reset_done")

	password_reset_form = PasswordResetForm()
	return render(request, 'password-reset.html', context={"password_reset_form":password_reset_form})

"""LOGIN-LOGOUT-REGISTER"""

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home') 

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
           user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username OR password does not exist')

    context = {'page': page} 
    return render(request, 'login-register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'login-register.html', {'form': form})

"""CHANGE - RESET - PASSWORD"""

@login_required
def password_change(request):
    agenda_objects = Agenda.objects.filter(user=request.user)
    form = PasswordChangeForm(request.user)
    context = {
        'form':form,
        'agenda_objects':agenda_objects,
        }
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            user_id = request.user.id
            success_url = reverse('user-profile', kwargs={'pk':user_id})
            return redirect(success_url)
    
        else:
            messages.error(request, 'Please correct the error below.')
    
    return render(request, 'password-change.html', context)

def password_reset(request):
    agenda_objects = Agenda.objects.filter(user=request.user)
    form = PasswordResetForm(request.user)
    context = {
        'form':form,
        'agenda_objects':agenda_objects,
        }
    if request.method == 'POST':
        form = PasswordResetForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
        else:
            messages.error(request, 'Please correct the error below.')
    
    return render(request, 'new_telegram_bot_service/password-reset-confirm.html', context)

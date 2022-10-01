from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib import messages
from .forms import SignUpForm

from django.contrib import sessions

class UserView(DetailView):
    template_name = 'users/profile.html'

    def get_object(self):
        return self.request.user


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('users:profile')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        if user and user.is_active:
            print('user is active')
            if user.groups.filter(name = 'therapist').exists():
                print('therapost')
                request.session['group'] = 'therapist'
                return HttpResponseRedirect('/therapist-appointments')
        else:
            messages.add_message(request, messages.INFO, 'Please enter a correct email and password. Note that, May be your account is disabled please contact us')
        return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form':form})

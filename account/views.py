from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm, MakePostForm

from django.shortcuts import redirect, render

# Create your views here.
def register(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_pass = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_pass)
            login(request, account)
            return redirect('home')
        else: # if Error
            context['registration_form'] = form
    else: # if GET
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register-form.html', context)

def logout_(request):
    logout(request)
    return redirect('login')

def login_(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            account = authenticate(email=email, password=password)
            if account:
                login(request, account)
                return redirect('home')
    else:
        form = AccountAuthenticationForm()
    
    context['login_form'] = form
    return render(request, 'login.html', context)

def account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                'email': request.POST['email'],
                'username': request.POST['username'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(
            initial={
                'email': request.user.email,
                'username': request.user.username,
            }
        )
    context['account_form'] = form
    return render(request, 'account.html', context)
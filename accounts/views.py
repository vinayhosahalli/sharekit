
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

# Create your views here.
from accounts.forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('index')
        messages.error(request, 'password fields didn’t match or username already exists')
    form = SignupForm()
    return render(request=request, template_name="accounts/signup.html", context={'signupform': form})


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('index')
        else:
            messages.error(request, "username or password is incorrect.")
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return render(request, 'accounts/login.html')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')

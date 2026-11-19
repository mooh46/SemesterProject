from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
from django.urls import reverse
from django.contrib.auth import login, logout,authenticate



def feed(request):
    return render(request,'photoApp/feed.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user  =  User.objects.create_user(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            login(request,user)
            return HttpResponseRedirect(reverse('feed'))
    else:
        form = RegisterForm()
    return  render(request,'photoApp/Register.html',{'form':form})

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request ,username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('feed'))
            form.add_error(None, "Invalid username and/or password.")
    else:
        form = LoginForm()
    return render(request,'photoApp/Login.html', {'form':form})


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
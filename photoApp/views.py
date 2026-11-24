from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
from django.urls import reverse
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



@login_required
def feed(request):
    posts = Post.objects.all().order_by('-date_posted')
    paginata =  Paginator(posts, 10)
    #request.GET gives us access to the url parameters and get, gets us the value of associated with page
    # then get_page takes that number and gets the value associated with that page
    #this gives us a page object with the number
    page_obj = paginata.get_page(request.GET.get('Page'))
    #from this Paginator object called paginata we use get_page which creates a Page object
    return render(request,'photoApp/feed.html',{'page_obj':page_obj})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            #create_user hashes our password before storing it
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
                #web has no memory between requests
                #when this runs django gives the  user a session id which is used to identify a row in a table in the database called django_session
                # which  has the user's userid so this session id is stored in a cookie in the browser
                # so the browser uses that id to get the user id which is then used to get a users details in users table
                login(request,user)
                return HttpResponseRedirect(reverse('feed'))
            form.add_error(None, "Invalid username and/or password.")
    else:
        form = LoginForm()
    return render(request,'photoApp/Login.html', {'form':form})


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse("feed"))

    else:
        form = PostForm()
    return render(request,'photoApp/new_post.html',{'form':form})


def profile(request,user_id):
    #a profile needs the username and the post right
    profile_user =  get_object_or_404(User,pk = user_id)
    posts = profile_user.posts.all().order_by('-date_posted')

    return render(request,"photoApp/profile.html",{
        "profile_user":profile_user,
        "posts":posts,
    })



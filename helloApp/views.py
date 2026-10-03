from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return  render(request, "helloApp/hello.html", {
        "greeting" : "Hello My name is Mohamed",
    })
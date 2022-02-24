from django.shortcuts import render, HttpResponse

# Create your views here.
def say_hello(request):
    "Requesting data from server"
    return HttpResponse("Hello!")
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "base.html")

def newspaper(request):
    return render(request, "newspaper.html")
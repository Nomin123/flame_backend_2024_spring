from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # name=request.GET.get("name") or "world"
    
    # print(request.Get["val1"])
    return HttpResponse("Hello, World!")
    
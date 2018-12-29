from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def login(request):
    # return HttpResponse("Hello 20171212")
    return render(request, "index.html")

def index(request):

    return render(request, "index1.html")


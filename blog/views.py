from django.shortcuts import render
from django.shortcuts import HttpResponse
from models import AlertReport

# Create your views here.
def updatees(request):
    return HttpResponse("hello updatees")

def login(request):
    # return HttpResponse("Hello 20171212")
    return render(request, "index.html")

def index(request):
    return render(request, "index1.html")


def search(request):
    return render(request, "index1.html")
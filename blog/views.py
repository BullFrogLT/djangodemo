#!/usr/bin/env python

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
    data = {}
    # all count
    data['result'] = AlertReport.objects.all()
    # ip count
    data['ipcount'] = data['result'].values('from_machine').distinct().order_by('from_machine').count()
    #


    return render(request, "search.html", {'data': data})


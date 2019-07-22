from django.http import HttpResponse
from django.shortcuts import render

def index_view(request):
    return render(request,'login.html')

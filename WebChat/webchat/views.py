from django.http import HttpResponse
from django.shortcuts import render

def index_view(request):
    # if request.method=='GET':
    #     return render(request,'index.html')
    # elif request.method =='POST':
    #     name=request.POST.get('name')
    #     password= request.POST.get('password')
    return render(request,'index.html')


def signup_view(request):        
    return render(request, 'signup.html')
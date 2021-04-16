from django.shortcuts import render
from django.http import HttpResponse
from app.forms import userForm
# Create your views here.


def test(test):
    return render(test,"suzhiyam.html",{'name':'Raam'})

def form(form):
    return render(form,"Register.html",{})

def result(result):
     
    
    return render(result,"result.html",{})
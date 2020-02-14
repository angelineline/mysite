from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Ange'})

def login_view(request):

    return render(request,'login.html',{'form':'form'})
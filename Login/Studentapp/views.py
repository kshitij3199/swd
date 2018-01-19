from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Studentclass
from django.contrib.auth import authenticate, login, logout

def index(request):
	return HttpResponse( '<h1>WELCOME TO SWD</h1><a href = "accounts/google/login" target = "_blank">login with gmail</a>')  

	
def detail(request):
	
	if request.user.is_authenticated:
		'''a = Studentclass()
		username = request.user.username
		a.namestudent = username
		a.save()'''
		
	
		return render(request, 'Studentapp/detail.html')
	else:
		HttpResponseRedirect("/")
		
	
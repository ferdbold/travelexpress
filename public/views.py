from django.shortcuts import render

def index(request):
	return render(request, 'public/index.html', {})

def login(request):
	return render(request, 'public/login.html', {})

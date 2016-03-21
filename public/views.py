from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index_view(request):
	return render(request, 'public/index.html', {})

def login_view(request):
	if (request.method == 'POST'):
		user = authenticate( \
			username = request.POST['username'], \
			password = request.POST['password'] \
		)

		if user is not None:
			login(request, user)
			return redirect('public:index')
		else:
			# TODO: Pass error message along with response
			return render(request, 'public/login.html', {})

	# GET requests
	else:
		return render(request, 'public/login.html', {})

def logout_view(request):
	logout(request)
	return redirect('public:index')

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
			return render(request, 'public/login.html', { \
				'alert': { \
					'type': 'danger', \
					'message': 'Erreur de connexion. Veuillez réessayer' \
				} \
			})

	# GET requests
	else:
		return render(request, 'public/login.html', {})

def logout_view(request):
	logout(request)
	return redirect('public:index')

def register_view(request):
	return render(request, 'public/register.html', {})

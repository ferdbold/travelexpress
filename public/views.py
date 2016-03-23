from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from public.models import CustomUser

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
	if(request.method == 'POST'):
		#validate passwords
		password1 = request.POST['password']
		password2 = request.POST['password_validation']

		if password1 == password2:
			CustomUser.objects.create_user ( \
				username = request.POST['username'], \
				first_name = request.POST['first_name'], \
				last_name = request.POST['last_name'], \
				password = request.POST['password'], \
				email = request.POST['email'], \
				phone = request.POST['phone'] \
			)
		else:
			return render(request, 'public/register.html', { \
				'alert': { \
					'type': 'danger', \
					'message': 'Erreur: les mots de passe ne correspondent pas' \
				} \
			})

	return render(request, 'public/register.html', {})

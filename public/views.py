from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import LoginForm, RegisterForm, TripForm

def index_view(request):
	return render(request, 'public/index.html', {})

def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			user = authenticate(
				username = request.POST['username'],
				password = request.POST['password']
			)

			if user is not None:
				login(request, user)
				return redirect('public:index')
			else:
				return render(request, 'public/login.html', {
					'alert': {
						'type': 'danger',
						'message': 'Authentication failed, please try again.'
					},
					'form': form
				})

	# GET requests
	else:
		form = LoginForm()

	return render(request, 'public/login.html', { 'form': form })

def logout_view(request):
	logout(request)
	return redirect('public:index')

def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)

		if form.is_valid():
			user = User.objects.create_user(
				username = form.cleaned_data.get('username'),
				email = form.cleaned_data.get('email'),
				password = form.cleaned_data.get('password'),
				first_name = form.cleaned_data.get('first_name'),
				last_name = form.cleaned_data.get('last_name')
			)
			profile = UserProfile(
				user = user,
				phone = form.cleaned_data.get('phone_number')
			)
			profile.save()

			user = authenticate(
				username = form.cleaned_data.get('username'),
				password = form.cleaned_data.get('password')
			)
			login(request, user)
			return redirect('public:index')

	# GET requests
	else:
		form = RegisterForm()

	return render(request, 'public/register.html', { 'form': form })

def trip_create_view(request):
	if request.method == 'POST':
		form = TripForm(request.POST)

		if form.is_valid():
			trip = form.save(commit=False)
			trip.driver = request.user
			trip.save()
			# TODO: Redirect to trip single page instead of index
			return render(request, 'public/index.html', {
				'alert': {
					'type': 'success',
					'message': 'Trip created successfully!'
				}
			})

	else:
		form = TripForm()

	return render(request, 'public/trip-create.html', { 'form': form })

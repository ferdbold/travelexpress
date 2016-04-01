from django.views.generic import View, DetailView, FormView, CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy

from .models import UserProfile, Trip
from .forms import RegisterForm

class IndexView(View):
	def get(self, request):
		latest_trips = Trip.objects.order_by('-id')[:5]
		return render(request, 'public/index.html', { 'latest_trips': latest_trips })

class LoginView(FormView):
	template_name = 'public/login.html'
	form_class = AuthenticationForm
	success_url = reverse_lazy('public:index')

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super(LoginView, self).form_valid(form)

class LogoutView(View):
	def get(self, request):
		logout(request)
		return redirect('public:index')

class RegisterView(FormView):
	template_name = 'public/register.html'
	form_class = RegisterForm
	success_url = reverse_lazy('public:index')

	def form_valid(self, form):
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
		login(self.request, user)

		return super(RegisterView, self).form_valid(form)

class TripCreateView(CreateView):
	model = Trip
	template_name = 'public/trip_new.html'
	fields = ['departure_date', 'origin', 'destination']
	success_url = reverse_lazy('public:index')

	def form_valid(self, form):
		trip = form.save(commit=False)
		trip.driver = self.request.user
		trip.save()

		return super(TripCreateView, self).form_valid(form)

class TripDetailView(DetailView):
	model = Trip

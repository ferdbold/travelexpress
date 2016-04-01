from django.conf.urls import url

from . import views

app_name = 'public'

urlpatterns = [
	url(r'^connexion/$', views.LoginView.as_view(), name='login'),
	url(r'^deconnexion/$', views.LogoutView.as_view(), name='logout'),
	url(r'^inscription/$', views.RegisterView.as_view(), name='register'),
	url(r'^voyage/creer/$', views.TripCreateView.as_view(), name='trip_create'),
	url(r'^$', views.IndexView.as_view(), name='index')
]

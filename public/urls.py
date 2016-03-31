from django.conf.urls import url

from . import views

app_name = 'public'

urlpatterns = [
	url(r'^connexion/$', views.login_view, name='login'),
	url(r'^deconnexion/$', views.logout_view, name='logout'),
	url(r'^inscription/$', views.register_view, name='register'),
	url(r'^voyage/creer/$', views.trip_create_view, name='trip_create'),
	url(r'^$', views.index_view, name='index')
]

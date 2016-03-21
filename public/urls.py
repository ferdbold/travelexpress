from django.conf.urls import url

from . import views

app_name = 'public'

urlpatterns = [
	url(r'^connexion/$', views.login, name='login'),
	url(r'^$', views.index, name='index')
]

from django.conf.urls import url

from . import views

app_name = 'public'

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^trips/new/$', views.TripCreateView.as_view(), name='trip_create'),
    url(r'^trips/(?P<pk>[0-9]+)/$', views.TripDetailView.as_view(), name='trip_detail'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.UserProfileView.as_view(), name='profile'),
    url(r'^$', views.IndexView.as_view(), name='index')
]

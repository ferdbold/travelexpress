from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView, RedirectView, DetailView, FormView, CreateView
from django.utils import timezone

from .forms import RegisterForm, PreferencesForm
from .models import UserProfile, Trip


class IndexView(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest_trips'] = Trip.objects.order_by('-id')[:5]
        return context


class LoginView(FormView):
    template_name = 'public/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('public:index')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    url = reverse_lazy('public:index')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class RegisterView(FormView):
    template_name = 'public/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('public:index')

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data.get('username'),
            email=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password'),
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name')
        )
        profile = UserProfile(
            user=user,
            phone=form.cleaned_data.get('phone')
        )
        profile.save()

        user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password')
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

    def get_context_data(self, **kwargs):
        context = super(TripDetailView, self).get_context_data(**kwargs)
        trip = Trip.objects.get(pk=kwargs['object'].pk)
        context['is_passenger'] = trip.passengers.filter(profile=self.request.user.profile).exists()
        if self.request.user.profile.blocked_until is not None:
            context['is_blocked'] = self.request.user.profile.blocked_until > timezone.now()
        else:
            context['is_blocked'] = False
        return context


class TripCancelView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('public:trip_detail',
                            kwargs={'pk': kwargs['pk']})

    def post(self, request, *args, **kwargs):
        trip = Trip.objects.get(pk=kwargs['pk'])
        trip.is_canceled = True
        trip.save()
        return super(TripCancelView, self).post(request, *args, **kwargs)


class TripJoinView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('public:trip_detail',
                            kwargs={'pk': kwargs['pk']})

    def post(self, request, *args, **kwargs):
        trip = Trip.objects.get(pk=kwargs['pk'])
        trip.passengers.add(request.user)
        trip.save()
        return super(TripJoinView, self).post(request, *args, **kwargs)


class TripQuitView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('public:trip_detail',
                            kwargs={'pk': kwargs['pk']})

    def post(self, request, *args, **kwargs):
        trip = Trip.objects.get(pk=kwargs['pk'])
        trip.passengers.remove(self.request.user)
        trip.save()
        userprofile = self.request.user.profile
        userprofile.quit_count += 1
        if userprofile.quit_count >= 3:
            userprofile.blocked_until = timezone.now() + timezone.timedelta(days=30)
            userprofile.quit_count = 0
        else:
            userprofile.blocked_until = timezone.now()
        userprofile.save()
        return super(TripQuitView, self).post(request, *args, **kwargs)


class UserProfileView(DetailView):
    model = User
    template_name = 'public/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)

        context['driver_trips'] = Trip.objects.filter(driver=context['object'])
        # TODO: Add passenger trips to context dictionary

        return context


class UserPreferencesView(LoginRequiredMixin, FormView):
    """Displays a form to edit user preferences. This view is only available to the current user."""
    template_name = 'public/user_preferences.html'
    form_class = PreferencesForm

    def get_success_url(self):
        """Redirect to my profile on success"""
        return reverse('public:profile', kwargs={'pk': self.request.user.id})

    def get_initial(self):
        """Prepopulate form data"""
        initial = super(UserPreferencesView, self).get_initial()
        user = self.request.user

        initial['first_name'] = user.first_name
        initial['last_name'] = user.last_name
        initial['email'] = user.email
        initial['phone'] = user.profile.phone
        initial['tolerates'] = user.profile.tolerates
        initial['does_not_tolerate'] = user.profile.does_not_tolerate

        return initial

    def form_valid(self, form):
        """Handle form submission"""
        user = self.request.user
        profile = user.profile

        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.email = form.cleaned_data.get('email')
        profile.phone = form.cleaned_data.get('phone')
        profile.tolerates = form.cleaned_data.get('tolerates')
        profile.does_not_tolerate = form.cleaned_data.get('does_not_tolerate')

        profile.save()
        user.save()

        return super(UserPreferencesView, self).form_valid(form)


class SearchResultsView(TemplateView):
    template_name = 'public/search_results.html'

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['search_from'] = self.request.GET.get('search_from')
        context['search_to'] = self.request.GET.get('search_to')

        if context['search_from'] != '':
            trips_from = Trip.objects.filter(origin=context['search_from'])
        if context['search_to'] != '':
            trips_to = Trip.objects.filter(destination=context['search_to'])

        if context['search_from'] != '' and context['search_to'] != '':
            trips = trips_from & trips_to
        elif context['search_from'] != '':
            trips = trips_from
        elif context['search_to'] != '':
            trips = trips_to
        else:
            trips = Trip.objects.all()

        context['trips'] = trips
        return context

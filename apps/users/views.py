from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic.base import RedirectView, TemplateView

from core.views import BaseView


class LoginView(BaseView):
    """View for users to log in."""

    menu = 'login'
    colors = ('#4A72B7', '#375d9e', '#fefefe')
    template_name = 'login.html'
    title = 'DK - Главная'
    description = 'DK - Войти'

    def post(self, request):
        """Get username and password to authenticate user."""
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_redirect = self.request.GET.get('next')
            return HttpResponseRedirect(
                next_redirect if next_redirect else reverse('main:index')
            )

        return HttpResponseRedirect(reverse('users:login'))


class SignUpView(TemplateView):
    """View for user to sign up.

    Currently this view is not used.

    """

    template_name = 'signup.html'
    description = 'DK - Зарегистрироваться'

    def get_context_data(self, **kwargs):
        """Get context data."""
        return {
            'title': 'Django Diary - Регистрация'
        }

    def post(self, request):
        """Get all user params to create user."""
        username = request.POST.get('username')
        email = request.POST.get('email')

        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')

        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            return HttpResponseRedirect(reverse('main:signup'))

        if User.objects.filter(email=email).exists():
            return HttpResponseRedirect(reverse('main:signup'))

        if password != password2:
            return HttpResponseRedirect(reverse('main:signup'))

        User.objects.create_user(
            username, email=email, password=password,
            first_name=firstname, last_name=lastname
        )

        return HttpResponseRedirect('/login')


class LogoutView(RedirectView):
    """View for users to log out."""

    url = '/'

    def get(self, request):
        """Log out current user."""
        logout(request)
        return super().get(request)

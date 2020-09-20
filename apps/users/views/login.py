from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect
from django.shortcuts import reverse

from core.views import BaseView


class LoginView(BaseView):
    """View for users to log in."""

    menu = 'profile'
    template_name = 'users/login.html'
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
                next_redirect if next_redirect else reverse('main:index'),
            )

        return HttpResponseRedirect(reverse('users:login'))

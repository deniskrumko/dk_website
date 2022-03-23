from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic.base import TemplateView


class SignUpView(TemplateView):
    """View for user to sign up.

    Currently this view is not used.

    """

    menu = 'user'
    template_name = 'users/signup.html'
    description = 'DK - Зарегистрироваться'

    def get_context_data(self, **kwargs):
        """Get context data."""
        return {
            'title': 'Django Diary - Регистрация',
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
            first_name=firstname, last_name=lastname,
        )

        return HttpResponseRedirect('/login')

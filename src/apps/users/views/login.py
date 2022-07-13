from django.contrib.auth import authenticate, login

from core.views import BaseView


class LoginView(BaseView):
    """View for users to log in."""

    menu = 'user'
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
            return self.redirect(next_redirect or 'main:index', use_reverse=not next_redirect)

        return self.redirect('users:login')

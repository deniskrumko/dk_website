from django.contrib.auth import logout
from django.views.generic.base import RedirectView


class LogoutView(RedirectView):
    """View for users to log out."""

    url = '/'

    def get(self, request):
        """Log out current user."""
        logout(request)
        return super().get(request)

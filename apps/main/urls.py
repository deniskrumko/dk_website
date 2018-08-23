from django.urls import path

from .views import IndexView, RedirectView

app_name = 'apps.main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('go/<page>/', RedirectView.as_view(), name='redirecting'),
]

from django.urls import path

from .views import IndexView

app_name = 'apps.main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

from django.urls import path

from . import views

app_name = 'apps.main'

urlpatterns = [
    # Main site page
    path('', views.IndexView.as_view(), name='index'),

    # Redirect page
    path('go/<page>/', views.RedirectView.as_view(), name='redirecting'),

    # Wake heroku app page
    path('wakemydyno.txt', views.WakeMyDyno.as_view(), name='awake')
]

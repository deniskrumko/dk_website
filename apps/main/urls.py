from django.urls import path

from . import views

app_name = 'apps.main'

urlpatterns = [
    # Main site page
    path('', views.IndexView.as_view(), name='index'),

    # Search pages
    path('search/', views.SearchView.as_view(), name='search_index'),
    path('search/<search_query>/', views.SearchView.as_view(), name='search'),

    # Redirect page
    path('go/<page>/', views.RedirectView.as_view(), name='redirecting'),

    # Wake heroku app page
    path('wakemydyno.txt', views.WakeMyDyno.as_view(), name='awake')
]

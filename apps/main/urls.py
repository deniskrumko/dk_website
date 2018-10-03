from django.urls import path

from .views import IndexView, RedirectView, SearchView

app_name = 'apps.main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search_index'),
    path('search/<search_query>/', SearchView.as_view(), name='search'),
    path('go/<page>/', RedirectView.as_view(), name='redirecting'),
]

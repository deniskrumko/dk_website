from django.urls import path

from .views import NewsView, NewsDetailView

app_name = 'apps.news'

urlpatterns = [
    path('', NewsView.as_view(), name='index'),
    path('<slug>/', NewsDetailView.as_view(), name='detail'),
]

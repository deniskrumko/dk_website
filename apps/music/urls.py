from django.urls import path

from . import views

app_name = 'apps.music'

urlpatterns = [
    path('', views.TrackIndexView.as_view(), name='index'),
    path('<slug>/', views.TrackDetailView.as_view(), name='detail'),
]

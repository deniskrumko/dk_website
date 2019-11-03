from django.urls import path

from . import views

app_name = 'apps.music'

urlpatterns = [
    path('', views.MusicIndexView.as_view(), name='index'),
    path('albums/<slug>/', views.AlbumDetailView.as_view(), name='detail'),
    path('tracks/', views.TracksView.as_view(), name='tracks'),
]

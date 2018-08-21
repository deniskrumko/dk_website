from django.urls import path

from .views import TrackListView

app_name = 'apps.music'

urlpatterns = [
    path('', TrackListView.as_view(), name='list'),
]

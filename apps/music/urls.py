from django.urls import path

from .views import TrackListView, TrackDetailsView

app_name = 'apps.music'

urlpatterns = [
    path('', TrackListView.as_view(), name='list'),
    path('<slug>/', TrackDetailsView.as_view(), name='details'),
]

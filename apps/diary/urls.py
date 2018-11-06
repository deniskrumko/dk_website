from django.urls import path

from . import views

app_name = 'apps.blog'

urlpatterns = [
    path('', views.DiaryIndexView.as_view(), name='index'),
    path('calendar/', views.DiaryCalendarView.as_view(), name='calendar'),
    path('tags/', views.DiaryTagsView.as_view(), name='tags'),
    path('tags/<tag>/', views.DiaryTagView.as_view(), name='tags-detail'),
    path('<date>/', views.DiaryDetailView.as_view(), name='detail'),
    path('<date>/edit/', views.DiaryEditView.as_view(), name='edit'),
]

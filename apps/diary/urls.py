from django.urls import path

from . import views

app_name = 'apps.blog'

urlpatterns = [
    path('', views.DiaryIndexView.as_view(), name='index'),
    path('date/<date>/', views.DiaryDetailView.as_view(), name='detail'),
    path('date/<date>/edit/', views.DiaryEditView.as_view(), name='edit'),
    path(
        'date/<date>/file_upload/',
        views.DiaryFileUploadView.as_view(),
        name='file_upload',
    ),
    path('search/', views.DiarySearchView.as_view(), name='search'),
    path('tags/', views.DiaryTagsIndexView.as_view(), name='tags'),
    path('tags/<tag>/', views.DiaryTagsDetailView.as_view(), name='tag'),
]

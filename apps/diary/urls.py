from django.urls import path

from . import views

app_name = 'apps.blog'

urlpatterns = [
    path('', views.DiaryIndexView.as_view(), name='index'),
    path('<date>/', views.DiaryDetailView.as_view(), name='detail'),
    path('<date>/edit/', views.DiaryEditView.as_view(), name='edit'),
]

from django.urls import path

from . import views

app_name = 'apps.blog'

urlpatterns = [
    path('', views.BlogIndexView.as_view(), name='index'),
    path('about/', views.AboutProjectView.as_view(), name='about'),
    path('<slug>/', views.BlogDetailView.as_view(), name='detail'),
]

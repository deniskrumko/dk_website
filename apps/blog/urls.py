from django.urls import path

from . import views

app_name = 'apps.blog'

urlpatterns = [
    path('', views.BlogIndexView.as_view(), name='index'),
    path('<slug>/', views.BlogDetailView.as_view(), name='detail'),
    path(
        '<slug>/download/',
        views.BlogDownloadView.as_view(),
        name='download'
    ),
]

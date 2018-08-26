from django.urls import path

from .views import IndexView, LikesView, RedirectView

app_name = 'apps.main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('go/<page>/', RedirectView.as_view(), name='redirecting'),
    path('likes/<obj_name>/<obj_id>/', LikesView.as_view(), name='likes')
]

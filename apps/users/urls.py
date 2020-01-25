from django.conf.urls import url

from .views import LoginView, LogoutView, ProfileView

app_name = 'apps.users'

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    # url(r'^signup/$', SignUpView.as_view(), name='signup'),
]

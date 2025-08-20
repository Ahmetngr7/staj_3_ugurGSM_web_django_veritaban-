from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('giris/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='giris'),
    path('cikis/', auth_views.LogoutView.as_view(next_page='accounts:giris'), name='cikis'),
    path('kayit/', auth_views.LoginView.as_view(template_name='accounts/reegister.html'), name='kayit'),

]



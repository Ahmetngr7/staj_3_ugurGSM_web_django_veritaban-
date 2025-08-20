from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.urun_listesi, name='liste'),
]

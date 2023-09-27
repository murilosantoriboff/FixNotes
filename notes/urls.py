from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('nova_categoria/', views.nova_categoria, name='nova_categoria'),
    path('nova_nota', views.nova_nota, name='nova_nota')
]
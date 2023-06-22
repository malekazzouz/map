from django.urls import path
from . import views

urlpatterns = [
    path('', views.map, name='map'),
    path('/admin', views.save_marker, name='save_marker'),
]
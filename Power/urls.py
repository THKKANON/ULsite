from django.urls import path

from . import views

app_name = 'Power'

urlpatterns = [
    path('', views.index, name = 'Power'),
    path('Band/create/', views.Band_create, name='Band_create'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('commons/', views.commons, name='commons'),
]

from django.urls import path
from . import views # need this to use views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]

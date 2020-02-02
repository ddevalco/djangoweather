from django.contrib import admin
from django.urls import path, include
from lookup import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lookup.urls')), #include lookup urls.py file
]

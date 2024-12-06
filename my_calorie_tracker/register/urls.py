from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register, name='register'),  # Używamy pustej ścieżki, ponieważ `/register/` jest przekierowane w głównym `urls.py`
    path('', include("django.contrib.auth.urls"))
]

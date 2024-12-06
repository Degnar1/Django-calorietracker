from django.urls import include, path
from . import views


urlpatterns = [
    # path('calorie_tracker/', views.calorie_tracker, name='calorie_tracker'),
    path('', views.home, name='home'),
    path('/about', views.about, name='about'),
    path('register/', include('register.urls')),
    # path('', include("django.contrib.auth.urls")),
]
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views


from calorie_tracker import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calorie_tracker.urls')), 
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
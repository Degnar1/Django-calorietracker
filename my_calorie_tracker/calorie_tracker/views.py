from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *

# def calorie_tracker(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())

def home(request):
    return render(request, 'base.html')

def about(request):
     return render(request, 'about.html')

def Register_view(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')
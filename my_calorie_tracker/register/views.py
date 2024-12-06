from django.shortcuts import render, redirect
# from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# def register(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # user = form.save()
#             # login(request, user)
#             return redirect('/home')  # Po udanej rejestracji przekierowanie na stronę główną
#     else:
#         form = RegisterForm()
#     return render(request, 'register/register.html', {'form': form})

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')    
        last_name = request.POST.get('last_name') 
        username = request.POST.get('username') 
        email = request.POST.get('email') 
        password = request.POST.get('password') 

        user_data_has_error = False

        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, "Username already exists")

        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, "Email already exists")

        if len(password) < 5:
            user_data_has_error = True
            messages.error(request, "Password must be at least 5 characters")

        if user_data_has_error:
            # Przekazujemy dane z powrotem do formularza
            return render(request, 'register.html', {
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'email': email
            })

        # Tworzenie nowego użytkownika
        new_user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )
        messages.success(request, 'Account created. Login now')
        return redirect('login')

    return render(request, 'register/register.html')


def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect ('login')
    return render(request, 'login.html')

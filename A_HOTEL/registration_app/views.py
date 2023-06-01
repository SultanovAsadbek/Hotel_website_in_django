from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
from django.template.loader import render_to_string

# Вход, выход, аутонтефикация пользователей.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Регистрация пользователей.
from registration_app.forms import RegisterForm
from registration_app.forms import LoginForm

from index_app.views import send_message


def register(request): 
    form = RegisterForm

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно.")
            
            name = form.cleaned_data['first_name']
            surname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            
            send = {
                "name": name,
                "surname": surname,
                "email": email,
                "date": datetime.datetime.now(),
            }
            
            print(send)
            html_body = render_to_string("reg_send_mail.html", send)
            send_message(html_body, "Регистрированный пользователь")
            
            return redirect("login")
    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, "register.html", context)


def loginUser(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"{request.user.first_name} {request.user.last_name} добро пожаловать.")
                return redirect("home")

            else:
                messages.error(request, "Проверьте пароль или имя пользователя!")
                # return render(request, "login.html", {"form": form})

    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def logoutUser(request):
    logout(request)
    messages.info(request, "Вы вышли из системы.")
    return redirect("home")

@login_required(login_url='login')
def profile(request):
    profile = request.user
    context = {"profile": profile}
    return render(request, 'profile.html', context)
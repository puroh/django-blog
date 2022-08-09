from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.forms import RegisterForm


def login_view(request):
    method = request.method
    if method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "welcome {}".format(user.username))
            return redirect("index")
        else:
            messages.error(request, "User or password no valid")

    return render(request, "login.html", {})


def logout_view(request):
    logout(request)
    messages.success(request, "User logout")
    return redirect("/users/login")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = form.save()
        if user:
            messages.success(
                request,
                "User created",
            )
            return redirect("index")

    return render(
        request,
        "register.html",
        {
            "form": form,
        },
    )

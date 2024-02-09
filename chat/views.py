from django.contrib.auth.decorators import login_required
from core.models import Message
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import SignUpForm, LoginForm


def register(request):
    msg = None

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Your account was created successfully.'
            messages.success(request, msg)

            return redirect("chat:login")
    else:
        form = SignUpForm()

    return render(request, "authentications/register.html", {"form": form, "msg": msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}

    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("chat:index")
        else:
            msg = 'Error validating the form'
            messages.error(request, msg)

    return render(request, "authentications/login.html", context)


def profile(request):
    return render(request, "layouts/base.html")


@login_required()
def index(request):
    return render(request, "home/index.html")


@login_required()
def room(request, room_name):
    messages_ = Message.objects.filter(room_name__room_name=room_name)[:10]

    return render(request, "home/room.html",
                  {"room_name": room_name,
                   "objects": messages_})

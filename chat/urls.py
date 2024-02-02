from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "chat"

urlpatterns = [
    path("", views.index, name="index"),
    path("chat/<str:room_name>/", views.room, name="room"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
]

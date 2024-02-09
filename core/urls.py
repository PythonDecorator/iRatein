"""
Users urls
"""

from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('profile/me/', views.ManageUserView.as_view(), name="me"),
    path('all/', views.AllUsers.as_view(), name="users"),
]

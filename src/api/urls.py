from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('users', views.Users.as_view()),
    path('users/<uuid:uuid>', views.UserInfo.as_view()),
    
    path('followers', views.Followers.as_view()),
    path('followers/<uuid:uuid>', views.Followers.as_view()),

    path('feed', views.Feed.as_view()),
    path('feed/<uuid:uuid>', views.Feed.as_view()),

    path('likes/<uuid:uuid>', views.Likes.as_view()),
]

from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="main"),
    # path("<int:page>", views.main, name="root_paginate"),
    path("author/<int:id>", views.get_author, name="get_author"),
]

from django.contrib import admin
from django.urls import path
from controllers.login import login
from controllers.sign_up import sign_up
from controllers.pocket_money import pocket_money
from controllers.budget import budget

urlpatterns = [
    path('login',login),
    path('sign_up',sign_up),
    path('pocket_money',pocket_money),
    path('budget',budget)
]
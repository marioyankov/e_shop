from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Group
from django.views import View

from rest_framework import views as rest_views, status, viewsets, permissions
from rest_framework.response import Response

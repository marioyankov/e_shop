from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Group
from django.views import View

from rest_framework import views as rest_views, status, viewsets, permissions
from rest_framework.response import Response
from .models import Product

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    # product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }

    return render(request, 'product_detail.html', context)
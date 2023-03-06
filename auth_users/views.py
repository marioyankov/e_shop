from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User, Group
from django.views import View

from rest_framework import views as rest_views, status, viewsets, permissions
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, UserProfileSerializer
from .forms import SignUpForm, UserProfileForm
from .models import UserProfile
from api_shop.models import Product

# Viewset to define the view behavior
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class SignUpUserView(rest_views.APIView):
    template_name = 'sign_up.html'

    def get(self, request):
        users = User.objects.all()
        serializer_context = {
            'request': request
        }
        serializer = UserSerializer(users, many=True, context=serializer_context)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            profile = UserProfile(
                user=user,
            )
            profile.user.groups.add(Group.objects.get(name='UserGroup'))
            profile.save()

            login(request, user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

# Django views
def index(request):
    products = Product.objects.all()

    context = {
        'products': products        
    }

    return render(request, 'core/base.html', context)


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': UserProfileForm(),
            'profile_user': user,
            'profile': user.userprofile,
            'posts': user.userprofile.post_set.all(),
        }
        return render(request, 'accounts/user_profile.html', context)
    else:
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('user profile')

        context = {
            'form': form,
        }

        return render(request, 'accounts/edit_profile.html', context)


def edit_profile(request, pk):
    user = request.user if pk is None else User.objects.get(pk=pk)
    # user = request.user.userprofile
    if request.method == 'GET':
        form = UserProfileForm(instance=user.userprofile)
        context = {
            'user': user,
            'form': form,
        }

        return render(request, 'accounts/edit_profile.html', context)

    else:
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('user profile')

        context = {
            'user': user,
            'form': form,
        }

        return render(request, 'accounts/edit_profile.html', context)


def sign_out_user(request):
    logout(request)
    return redirect('index')

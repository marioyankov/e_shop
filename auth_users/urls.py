from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet, GroupViewSet, UserProfileViewSet, SignUpUserView, sign_out_user, user_profile, edit_profile, index


# Router to provide easy way to automatically determin the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'profiles', UserProfileViewSet)

urlpatterns = [
    path('', index, name='home'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', SignUpUserView.as_view(), name='sign up user'),
    path('profile/', user_profile, name='user profile'),
    path('profile/<int:pk>/', user_profile, name='user profile'),
    path('edit_profile/<int:pk>/', edit_profile, name='edit profile'),
    path('signout/', sign_out_user, name='sign out user'),
]

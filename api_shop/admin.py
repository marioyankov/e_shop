from django.contrib import admin
from .models import UserProfile

class ViewUser(admin.ModelAdmin):
    list_display = ('id', 'user')


admin.site.register(UserProfile, ViewUser)
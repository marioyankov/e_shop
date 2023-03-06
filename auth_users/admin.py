from django.contrib import admin
from .models import UserProfile, BusinessProfile

class UserViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    prepopulated_fields = {"slug": ("first_name", "last_name")}

class BusinessUserViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(UserProfile, UserViewAdmin)
admin.site.register(BusinessProfile, BusinessUserViewAdmin)
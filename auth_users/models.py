from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=10)
    slug = models.SlugField(null=False, unique=True)
    
    def ifExists(self):
        if UserProfile.objects.filter(user=self.user):
            return True
        
        return False

    def __str__(self):
        return self.user.username

# Create model for bussiness profile
class BusinessProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True)
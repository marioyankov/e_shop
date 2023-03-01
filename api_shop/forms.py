from django import forms
from django.contrib.auth.forms import UserCreationForm
from .FormControlMixin import FormControlMixin
from .models import UserProfile

class SignUpForm(FormControlMixin, UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields_()

class UserProfileForm(FormControlMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__init_fields__()
    
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'profile_img')

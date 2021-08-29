from django.db.models import fields
from django.forms import ModelForm
from accounts.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

class CustomerProfile(ModelForm):
    class Meta:
        model=Customer
        fields=['email','phone','profile_pic']

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from .models import OrderRegistration
#from django.core.validators import RegexValidator
#from django_countries.fields import CountryField
#from django.utils.translation import gettext_lazy as _


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','password1','password2', 'first_name','last_name']


# class RegistrationForm(OrderRegistration):
#     class Meta:
#         db_table = 'OrderRegistration'             
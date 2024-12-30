from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Employee

# User registration form
class RegisterForm(UserCreationForm):
    class Meta: 
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

# Employee form 
class EmployeeForm(forms.ModelForm):
    class Meta: 
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'position', 'salary']
        
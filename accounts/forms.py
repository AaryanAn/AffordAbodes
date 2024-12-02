from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Custom user creation form for handling user registration
class CustomUserCreationForm(UserCreationForm):
    # Inner Meta class defines metadata for the form
    class Meta:
        model = User  # Links the form to Django's built-in User model
        fields = ('username', 'email', 'password1', 'password2')  # Fields to display and manage in the form
        
        # Custom labels for better user experience
        labels = {
            "username": "Username",  # Label for the username field
            "email": "Email address",  # Label for the email field
            "password1": "Password",  # Label for the password field
            "password2": "Confirm password"  # Label for the password confirmation field
        }
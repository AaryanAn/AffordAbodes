from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Handles user registration
def register(request):
    if request.method == 'POST':  # If the form is submitted
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  # Validate form data
            user = form.save()  # Save the new user
            login(request, user)  # Log in the new user
            return redirect('welcome')  # Redirect to the welcome page
    else:
        form = CustomUserCreationForm()  # Provide an empty form for GET requests
    return render(request, 'registration/register.html', {'form': form})

# Displays the welcome page for logged-in users
@login_required
def welcome_view(request):
    return render(request, 'welcome.html', {'username': request.user.username})

# Renders the contact page
class ContactView(TemplateView):
    template_name = 'contact.html'

# Renders the FAQ page
class FaqView(TemplateView):
    template_name = 'faq.html'

# Custom login view to handle user authentication
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Specifies the login template

    # Redirects to the welcome page on successful login
    def get_success_url(self):
        return reverse_lazy('welcome')

    # Adds an error message for invalid login attempts
    def form_invalid(self, form):
        messages.error(self.request, "No user found. Please check your credentials or create an account.")
        return super().form_invalid(form)

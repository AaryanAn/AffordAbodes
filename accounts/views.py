from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def welcome_view(request):
    return render(request, 'welcome.html', {'username': request.user.username})

class ContactView(TemplateView):
    template_name = 'contact.html'

class FaqView(TemplateView):
    template_name = 'faq.html'

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    def get_success_url(self):
        return reverse_lazy('welcome')

    
    def form_invalid(self, form):
        messages.error(self.request, "No user found. Please check your credentials or create an account.")
        return super().form_invalid(form)
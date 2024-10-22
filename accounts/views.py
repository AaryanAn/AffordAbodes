from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your desired page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class ContactView(TemplateView):
    template_name = 'contact.html'

class FaqView(TemplateView):
    template_name = 'faq.html'
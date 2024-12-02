from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import register, ContactView, FaqView, CustomLoginView, welcome_view

urlpatterns = [
    # Custom login view for handling user login
    path('login/', CustomLoginView.as_view(), name='login'),
    
    # Default logout view from Django for user logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Registration view for new user sign-up (ensure `register` is implemented in views)
    path('register/', views.register, name='register'),
    
    # Password reset process - Step 1: Request password reset
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    # Password reset process - Step 2: Notification that reset email has been sent
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    
    # Password reset process - Step 3: Reset link confirmation (uidb64 and token are placeholders for user ID and token)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    # Password reset process - Step 4: Confirmation of successful password reset
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # Contact page view
    path('contact/', views.ContactView.as_view(), name='contact'),
    
    # FAQ page view
    path('faq/', views.FaqView.as_view(), name='faq'),
    
    # Welcome page view
    path('welcome/', views.welcome_view, name='welcome'),
]

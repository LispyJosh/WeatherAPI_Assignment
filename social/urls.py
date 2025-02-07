from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth.views import (
    LogoutView, 
    LoginView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView
)
from . import views

# Custom home view to handle redirection
def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('index')  # Redirect to weather app homepage
    return redirect('login')  # Redirect to login page if not logged in

urlpatterns = [
    # Root URL -> Redirects based on authentication status
    path('', home_redirect, name='home'),

    # Profile-related views
    path('profile/edit/', views.edit_account, name='edit_account'),  
    path('profile/<str:username>/', views.profile, name='profile'),  
    path('profile/', views.default_profile, name='default_profile'),  

    # Authentication - Login & Logout
    path('login/', LoginView.as_view(template_name='social/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Registration - User sign-up
    path('register/', views.register, name='register'),

    # Forgot Email - Allows users to retrieve their email
    path('forgot_email/', views.forgot_email, name='forgot_email'),

    # Password reset functionality
    path('password-reset/', PasswordResetView.as_view(
        template_name='social/password_reset.html'
    ), name='password_reset'),
    
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='social/password_reset_done.html'
    ), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='social/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='social/password_reset_complete.html'
    ), name='password_reset_complete'),
]

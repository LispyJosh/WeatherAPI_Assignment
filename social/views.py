from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Profile
from .forms import ProfileUpdateForm, CustomUserCreationForm, ForgotEmailForm

# Home View - Redirect users based on authentication status
def home(request):
    if request.user.is_authenticated:
        return redirect('weather_home')  # Redirect logged-in users to weather app
    return redirect('login')  # Redirect logged-out users to login page

# Profile View
@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'social/profile.html', {'profile': profile})

# Default Profile View
@login_required
def default_profile(request):
    profile = request.user.profile
    return render(request, 'social/profile.html', {'profile': profile})

# Edit Account View
@login_required
def edit_account(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('default_profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'social/edit_account.html', {'form': form})

# Registration View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'social/register.html', {'form': form})

# Base View
def base(request):
    return render(request, 'social/base.html')

# Forgot Email View
def forgot_email(request):
    if request.method == 'POST':
        form = ForgotEmailForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                user = User.objects.get(username=username)
                if not user.email:
                    messages.error(request, 'No email associated with this account.')
                else:
                    send_mail(
                        'Your Registered Email',
                        f'Hello {user.username}, your registered email address is: {user.email}',
                        settings.DEFAULT_FROM_EMAIL,
                        [user.email],
                        fail_silently=False,
                    )
                    messages.success(request, 'An email with your registered email address has been sent.')
                    return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'No account found with that username.')
            except Exception as e:
                messages.error(request, 'An unexpected error occurred. Please try again later.')
                print(f"Error in forgot_email view: {e}")
    else:
        form = ForgotEmailForm()
    return render(request, 'social/forgot_email.html', {'form': form})

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

urlpatterns = [
    # Home page displaying posts
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

    # Edit profile must come before profile/<str:username> to avoid conflicts
    path('profile/edit/', views.edit_account, name='edit_account'),

    # Profile page for a specific user
    path('profile/<str:username>/', views.profile, name='profile'),

    # Default profile view if no username is provided
    path('profile/', views.default_profile, name='default_profile'),

    # User's message inbox
    path('messages/', views.message_list, name='message_list'),
    path('messages/new/', views.new_message, name='new_message'),
    path('messages/<str:username>/', views.conversation, name='conversation'),
    path('base/', views.base, name='base'),

    # Login and logout routes
    path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Registration route
    path('register/', views.register, name='register'),

    # Forgot Email route
    path('forgot_email/', views.forgot_email, name='forgot_email'),

    # Password reset routes (Django built-in views)
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

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Message, Profile

# Form for creating a new post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']

# Form for sending a new message
class MessageForm(forms.ModelForm):
    recipient = forms.CharField(
        max_length=150, 
        label="Recipient Username",
        help_text="Enter the username of the person you want to message."
    )

    class Meta:
        model = Message
        fields = ['recipient', 'content']

    def clean_recipient(self):
        username = self.cleaned_data.get('recipient')
        try:
            recipient = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("The specified user does not exist.")
        return recipient

# Form for updating user profile (bio and profile picture)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']

# Custom Registration Form - Makes Email Mandatory
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# Forgot Email Form
class ForgotEmailForm(forms.Form):
    username = forms.CharField(
        max_length=150, 
        label="Username",
        help_text="Enter your username to recover your registered email."
    )

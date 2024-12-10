from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.db.models import Q
from .models import Profile, Post, Message, Comment
from .forms import PostForm, MessageForm, ProfileUpdateForm, CustomUserCreationForm, ForgotEmailForm

# Home View - Display all posts
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'social/home.html', {'posts': posts})

# Profile View - Displays user profile and their posts
@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    posts = Post.objects.filter(user=user).order_by('-created_at')
    return render(request, 'social/profile.html', {'profile': profile, 'posts': posts})

# Default Profile View - For cases where no username is provided
@login_required
def default_profile(request):
    profile = request.user.profile
    posts = Post.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'social/profile.html', {'profile': profile, 'posts': posts})

# Edit Account View - Allows users to update their profile picture and bio
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

# Post Detail View - Displays a single post and its comments
@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-timestamp')
    return render(request, 'social/post_detail.html', {'post': post, 'comments': comments})

# New Post View - Allows users to create a new post
@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'social/new_post.html', {'form': form})

# Message List View (Inbox) - Displays messages for the logged-in user
@login_required
def message_list(request):
    all_messages = Message.objects.filter(Q(sender=request.user) | Q(recipient=request.user)).order_by('-timestamp')

    conversations = {}
    for message in all_messages:
        other_user = message.recipient if message.sender == request.user else message.sender
        if other_user not in conversations:
            conversations[other_user] = message

    formatted_conversations = [{'other_user': user, 'message': msg} for user, msg in conversations.items()]
    return render(request, 'social/message_list.html', {'conversations': formatted_conversations})

# New Message View - Allows users to send a new message
@login_required
def new_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            recipient_username = form.cleaned_data['recipient']
            try:
                recipient_user = User.objects.get(username=recipient_username)
                message.recipient = recipient_user
                message.save()
                messages.success(request, 'Message sent successfully!')
                return redirect('message_list')
            except User.DoesNotExist:
                messages.error(request, 'Recipient does not exist.')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = MessageForm()
    return render(request, 'social/new_message.html', {'form': form})

# Conversation View - Displays a conversation between two users
@login_required
def conversation(request, username):
    other_user = get_object_or_404(User, username=username)
    messages_queryset = Message.objects.filter(
        Q(sender=request.user, recipient=other_user) | Q(sender=other_user, recipient=request.user)
    ).order_by('id')  # Order by ID instead of timestamp to avoid using time-related fields

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender = request.user
            new_message.recipient = other_user
            new_message.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('conversation', username=username)
        else:
            messages.error(request, 'Failed to send the message. Please try again.')
    else:
        form = MessageForm(initial={'recipient': other_user.username})

    return render(
        request,
        'social/conversation.html',
        {
            'messages': messages_queryset,
            'form': form,
            'other_user': other_user,
        }
    )


# Registration View - Handles user registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'social/register.html', {'form': form})

# Base View - For testing base.html
def base(request):
    return render(request, 'social/base.html')

# Forgot Email View - Allows users to recover their registered email
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

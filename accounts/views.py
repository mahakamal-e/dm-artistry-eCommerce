"""
Views for user authentication and profile management.
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import update_session_auth_hash
from .forms import CreateUserForm, PasswordChangeForm
from accounts.models import UserProfile


def register(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}')
            return redirect('login')
    else:
        form = CreateUserForm()
        
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def my_login(request):
    """
    Handles user login.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                return redirect('/admin')
            else:
                return redirect('profile')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login')

    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

@login_required
def custom_logout(request):
    """
    Handles user logout.
    """
    auth_logout(request)
    return redirect('home')

@login_required
def profile(request):
    """
    Displays and updates user profile information.
    """
    profile = None
    password_form = None

    if not request.user.is_superuser:
        try:
            profile = request.user.userprofile
        except UserProfile.DoesNotExist:
            profile = None

    if request.method == 'POST':
        if 'first_name' in request.POST:
            request.user.first_name = request.POST['first_name']
            request.user.last_name = request.POST['last_name']

            if profile:
                profile.phone_number = request.POST['phone_number']
                profile.address_line1 = request.POST['address_line1']
                profile.address_line2 = request.POST['address_line2']
                profile.postcode = request.POST['postcode']
                profile.state = request.POST['state']
                profile.country = request.POST['country']
                profile.save()

            request.user.save()
            messages.success(request, 'Profile updated successfully!')

        if 'old_password' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)

            if password_form.is_valid():
                try:
                    user = password_form.save()
                    update_session_auth_hash(request, user)
                    messages.success(request, 'Your password has been updated successfully!')
                    return redirect('profile')
                except Exception as e:
                    messages.error(request, f"Error: {str(e)}")
            else:
                messages.error(request, 'Please correct the error below.')

    if not password_form:
        password_form = PasswordChangeForm(request.user)

    context = {
        'user': request.user,
        'profile': profile,
        'password_form': password_form
    }
    return render(request, 'accounts/profile.html', context)


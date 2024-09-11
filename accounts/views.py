from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from accounts.models import UserProfile


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = CreateUserForm()  # Initialize an empty form for GET request
        
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin')
            else:
                return redirect('profile')
        else:
            # Add an error message if authentication fails
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login')  # Redirect back to login page

    else:
        form = AuthenticationForm()  # Initialize the form for GET request
    
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

@login_required
def custom_logout(request):
    auth_logout(request)
    return redirect('home')


@login_required
def profile(request):
    profile = None  # Initialize profile variable
    password_form = None  # Initialize the password_form variable

    # Get user profile only if not a superuser
    if not request.user.is_superuser:
        try:
            profile = request.user.userprofile  # Access the user profile directly
        except UserProfile.DoesNotExist:
            profile = None  # Handle missing profile

    # Handle POST requests
    if request.method == 'POST':
        # If the user is updating profile information
        if 'first_name' in request.POST:
            # Update user information directly, without .get() on request.user
            request.user.first_name = request.POST['first_name']  # Directly access POST data
            request.user.last_name = request.POST['last_name']

            # Update profile fields if the profile exists
            if profile:
                profile.phone_number = request.POST['phone_number']
                profile.address_line1 = request.POST['address_line1']
                profile.address_line2 = request.POST['address_line2']
                profile.postcode = request.POST['postcode']
                profile.state = request.POST['state']
                profile.country = request.POST['country']
                profile.save()  # Save profile updates

            request.user.save()  # Save user updates
            messages.success(request, 'Profile updated successfully!')

        # If the user is changing their password
        if 'old_password' in request.POST:  # Password change form submitted
            password_form = PasswordChangeForm(request.user, request.POST)

            # Check if form data is being processed correctly
            if password_form.is_valid():
                try:
                    user = password_form.save()  # Update password
                    update_session_auth_hash(request, user)  # Keep the user logged in
                    messages.success(request, 'Your password has been updated successfully!')
                    return redirect('profile')
                except Exception as e:
                    messages.error(request, f"Error: {str(e)}")  # Handle errors gracefully
            else:
                messages.error(request, 'Please correct the error below.')

    # Initialize the password change form if not set
    if not password_form:
        password_form = PasswordChangeForm(request.user)

    context = {
        'user': request.user,
        'profile': profile,
        'password_form': password_form  # Passing password change form to the template
    }
    return render(request, 'accounts/profile.html', context)




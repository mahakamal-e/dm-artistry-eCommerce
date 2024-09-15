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
from orders.models import Order


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
    # Initialize variables
    profile = None
    password_form = None

    # Check if the user has a profile; if not, create one
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # Create a new profile if it does not exist
        profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        # Handle profile updates
        if 'first_name' in request.POST:
            request.user.first_name = request.POST.get('first_name', '')
            request.user.last_name = request.POST.get('last_name', '')
            request.user.save()
            messages.success(request, 'Profile information updated successfully!')

            if profile:
                profile.phone_number = request.POST.get('phone_number', '')
                profile.address_line1 = request.POST.get('address_line1', '')
                profile.address_line2 = request.POST.get('address_line2', '')
                profile.postcode = request.POST.get('postcode', '')
                profile.state = request.POST.get('state', '')
                profile.country = request.POST.get('country', '')
                profile.save()

        # Handle password change
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
                messages.error(request, 'Please correct the errors below.')

    if not password_form:
        password_form = PasswordChangeForm(request.user)
        
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'user': request.user,
        'profile': profile,
        'password_form': password_form,
        'orders': orders
    }
    return render(request, 'accounts/profile.html', context)

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout, login
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import logout as auth_logout


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
                return redirect('home')
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


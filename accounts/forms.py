from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import re


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        error_messages = {
            'username': {
                'required': 'Please enter a username.',
            },
            'email': {
                'required': 'Please enter an email address.',
            },
            'password1': {
                'required': 'Please enter a password.',
            },
            'password2': {
                'required': 'Please confirm your password.',
            }
        }

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose a different one.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered. Please use a different email.")
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if password:
            errors = []
            if len(password) < 8:
                errors.append("Your password must be at least 8 characters long.")
            if not re.search(r'[A-Z]', password):
                errors.append("Your password must include at least one uppercase letter.")
            if not re.search(r'[a-z]', password):
                errors.append("Your password must include at least one lowercase letter.")
            if not re.search(r'[0-9]', password):
                errors.append("Your password must include at least one digit.")
            if not re.search(r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/\\|`~]', password):
                errors.append("Your password must include at least one special character.")
            if errors:
                raise forms.ValidationError(errors)
        return password

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    

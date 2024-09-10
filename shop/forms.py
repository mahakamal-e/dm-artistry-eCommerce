from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address_line1', 'address_line2', 'postcode', 'state', 'country']

class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'}))

    def __init__(self, user, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.user = user

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not check_password(old_password, self.user.password):
            raise forms.ValidationError("Old password is incorrect.")
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("New passwords do not match.")
        
        # Add any other password validation rules here (e.g., complexity checks)
        
        return cleaned_data

    def save(self):
        new_password = self.cleaned_data.get('new_password1')
        self.user.set_password(new_password)
        self.user.save()
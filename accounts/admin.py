from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

# Customize the Django admin site titles
admin.site.site_header = "D&M Artistry E-Commerce"  # Header title at the top of the admin interface
admin.site.site_title = "Admin Dashboard"  # Title in the browser tab
admin.site.index_title = "Welcome to Admin Dashboard"  # Title on the admin home page

class UserProfileInline(admin.StackedInline):
    """
    Inline admin interface for managing UserProfile associated with a User,
    it means that can't add user profile without creating user first
    """
    model = UserProfile
    can_delete = False # Prevent deletion of UserProfile through the User admin interface
    fields = ['phone_number', 'address_line1', 'address_line2', 'postcode', 'state', 'country']
    extra = 0  # No extra forms for inline by default

class CustomUserAdmin(UserAdmin):
    """Customized admin interface for the User model."""
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )

    inlines = [UserProfileInline]  # Include UserProfileInline in the User admin

class UserProfileAdmin(admin.ModelAdmin):
    """Admin interface for managing UserProfile model."""
    list_display = ('user', 'phone_number', 'address_line1', 'postcode', 'state', 'country')
    search_fields = ('user__username', 'user__email', 'phone_number')
    list_filter = ('state', 'country')


admin.site.unregister(User)  # Unregister the default User admin to cutomized
admin.site.register(User, CustomUserAdmin)  # Register the User model with CustomUserAdmin
# Register the UserProfile model with UserProfileAdmin
admin.site.register(UserProfile, UserProfileAdmin)

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

admin.site.site_header = "D&M Artistry E-Commerce"  # Default title at the top
admin.site.site_title = "Admin Dashboard"  # Title in the browser tab
admin.site.index_title = "Welcome to Admin Dashboard"

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fields = ['phone_number', 'address_line1', 'address_line2', 'postcode', 'state', 'country']
    extra = 0

class CustomUserAdmin(UserAdmin):
    # Define fields to display in the admin interface
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')

    # Include fields to be used in the admin form
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

# Register the user model with the customized admin interface
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address_line1', 'postcode', 'state', 'country')
    search_fields = ('user__username', 'user__email', 'phone_number')
    list_filter = ('state', 'country')
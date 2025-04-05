from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "email", "is_staff", "is_active")
    list_filter = ("username", "email", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "email")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (None, {"fields": ("username", "email")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )

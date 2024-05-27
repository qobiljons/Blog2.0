from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreateForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "first_name", "last_name", "email", "date_of_birth"]

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth",)}),  # Ensure 'date_of_birth' is a tuple
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth",)}),  # Ensure 'date_of_birth' is a tuple
    )


admin.site.register(CustomUser, CustomUserAdmin)

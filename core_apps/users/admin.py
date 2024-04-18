from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _lazy

from .forms import UserChangeForm, UserCreationForm
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    form = UserChangeForm
    add_form = UserCreationForm
    ordering = ['email']

    list_display = ["id_key", "id", "email", "is_staff", "is_active"]
    list_display_links = ["id_key", "id", "email"]
    list_filter = ['email', 'is_staff', 'is_active']

    fieldsets = [
        (_lazy('Login Credentials'), {'fields': ['email', 'password']}),
        (_lazy('Permissions'), {'fields': ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions']}),
        (_lazy('Dates'), {'fields': ['last_login', 'join_date']}),
    ]

    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': ['email', 'password1', 'password2'],
        }),
    ]


admin.site.register(User, CustomUserAdmin)

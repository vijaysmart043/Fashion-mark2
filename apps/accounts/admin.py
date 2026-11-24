from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'mobile', 'is_mobile_verified', 'is_staff')
    search_fields = ('email', 'username', 'mobile')
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Info'), {'fields': ('mobile', 'is_mobile_verified', 'date_of_birth')}),
    )

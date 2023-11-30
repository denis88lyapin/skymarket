from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'first_name', 'last_name', 'phone', 'is_active', 'role',)
    list_filter = ('email', 'role',)
    search_fields = ('email', 'role',)

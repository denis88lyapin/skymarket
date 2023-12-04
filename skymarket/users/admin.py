from django.contrib import admin
from .models import User
from django.utils.translation import gettext_lazy as _


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'email', 'first_name', 'last_name', 'phone', 'is_active', 'role',)
#     list_filter = ('email', 'role',)
#     search_fields = ('email', 'role',)
#
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Personal Info'), {'fields': ('first_name', 'last_name', 'phone', 'image')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#         (_('User Role'), {'fields': ('role',)}),
#     )
#
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )

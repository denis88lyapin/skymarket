from django.contrib import admin
from .models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'price', 'description', 'author', 'created_at',)
    list_filter = ('title', 'price', 'author',)
    search_fields = ('title', 'price', 'author',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'ad', 'created_at',)
    list_filter = ('author', 'ad', 'created_at',)
    search_fields = ('text', 'author', 'ad',)

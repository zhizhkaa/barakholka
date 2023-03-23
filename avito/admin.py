import email
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'surname',
        'phone_number', 'birth_date'
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'email')
        }),
        ('Личная информация', {
            'fields': ('first_name', 'last_name', 'surname', 'birth_date', 'phone_number')
        }),
        ('Разрешения', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Важные даты', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2', 'email')
        }),
        ('Личная информация', {
            'fields': ('first_name', 'last_name', 'surname', 'birth_date', 'phone_number')
        }),
        ('Разрешения', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id', 'user', 'user_comment', 'rating', 'created')
    list_filter = ("created", "rating")
    search_fields = ['user', 'user_who']

admin.site.register(Comment, CommentAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_id', 'city', 'street', 'number')
    list_filter = ('city', 'street', 'number')
    search_fields = ['city', 'street', 'number']

admin.site.register(Address, AddressAdmin)
admin.site.register(City)
admin.site.register(Street)

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'title', 'seller', 'price', 'category', 'status')

admin.site.register(Post, PostAdmin)

admin.site.register(PostCategory)

admin.site.register(PostStatus)

class DealAdmin(admin.ModelAdmin):
    list_display = ('deal_id', 'post', 'buyer', 'status', 'date')

admin.site.register(Deal, DealAdmin)

admin.site.register(DealStatus)

class FileAdmin(admin.ModelAdmin):
    list_display = ('post', 'link')
    
admin.site.register(File, FileAdmin)












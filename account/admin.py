# core/admin.py
from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import UserProfile, Account

class CustomAdminSite(AdminSite):
    site_header = 'WIKITUBE ADMIN'
    site_title = 'WIKITUBE'
    index_title = 'Welcome to WIKITUBE'

custom_admin_site = CustomAdminSite(name='custom_admin')

class UserProfileAdmin(admin.ModelAdmin):
    pass

class AccountAdmin(admin.ModelAdmin):
    pass

custom_admin_site.register(UserProfile, UserProfileAdmin)
custom_admin_site.register(Account, AccountAdmin)

from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class MyUserAdmin(UserAdmin):

  fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('grade',)}),
    )

admin.site.register(User, MyUserAdmin)
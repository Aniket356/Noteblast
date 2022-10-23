from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.

class MyUserAdmin(UserAdmin):
  form = CustomUserChangeForm
  add_form = CustomUserCreationForm

  fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('grade',)}),
    )

admin.site.register(User, MyUserAdmin)
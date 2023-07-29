from django.contrib import admin
from home.models import Regular_user
# Register your models here.

admin.site.register(Regular_user)


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# class Regular_userAdmin(UserAdmin):
#     add_form = UserCreationForm
#     form = UserChangeForm
#     model = Regular_user
#     list_display = ['pk', 'email', 'username', 'first_name', 'last_name']
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('email', 'first_name', 'last_name',)}),
#     )
#     fieldsets = UserAdmin.fieldsets


# admin.site.register(Regular_user, Regular_userAdmin)
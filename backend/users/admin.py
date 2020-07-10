from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class AccountAdmin(UserAdmin):
    list_display = (
        'pk', 'username', 'email', 'name', 'surname', 'birthday', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username', 'birth_date')
    readonly_fields = ('pk', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, AccountAdmin)

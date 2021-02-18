from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Report, BlackList, Friend, Like, BannedIp


class AccountAdmin(UserAdmin):
    list_display = (
        'pk', 'username', 'email', 'name', 'surname', 'birthday', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    # search_fields = ('email', 'username', 'birth_date')
    readonly_fields = ('pk', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, AccountAdmin)

admin.site.register(Report, list_display=['pk', 'status', 'reason', 'reporting', 'reported'],
                    readonly_fields=['pk', 'reporting', 'reported', 'reason', 'description'])

admin.site.register(BlackList, list_display=['pk', 'user', 'blacklisted'],
                    readonly_fields=['pk', 'user', 'blacklisted'])

admin.site.register(Friend, list_display=['pk', 'user', 'friend', 'status'],
                    readonly_fields=['pk', 'user', 'friend', 'status'])

admin.site.register(Like, list_display=['pk', 'liked_by', 'liked', 'value'],
                    readonly_fields=['pk', 'liked_by', 'liked', 'value'])

admin.site.register(BannedIp, list_display=['pk', 'ip'],
                    readonly_fields=['pk', 'ip'])

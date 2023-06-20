from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models

admin.site.site_title = 'Administration'
admin.site.site_header = 'Administration'
admin.site.index_title = 'Dashboard'


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "username", "email", "password1", "password2"),
            },
        ),
    )

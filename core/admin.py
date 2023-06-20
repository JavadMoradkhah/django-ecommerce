from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

admin.site.site_title = 'Administration'
admin.site.site_header = 'Administration'
admin.site.index_title = 'Dashboard'

admin.site.register(models.User, UserAdmin)

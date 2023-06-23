from django.contrib import admin
from . import models

LIST_PER_PAGE = 10


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')
    search_fields = ['name']
    prepopulated_fields = {"slug": ["name"]}
    autocomplete_fields = ['parent']
    list_select_related = ['parent']
    list_per_page = LIST_PER_PAGE


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ['name']
    prepopulated_fields = {"slug": ["name"]}
    list_per_page = LIST_PER_PAGE
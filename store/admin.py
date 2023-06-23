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


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'shippable']
    search_fields = ['name']
    ordering = ['name']
    list_per_page = LIST_PER_PAGE


@admin.register(models.FaqCategory)
class FaqCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']
    list_per_page = LIST_PER_PAGE


@admin.register(models.FAQ)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['question', 'category']
    search_fields = ['question']
    autocomplete_fields = ['category']
    list_select_related = ['category']
    ordering = ['question']
    list_per_page = LIST_PER_PAGE


@admin.register(models.ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_active']
    search_fields = ['name']
    ordering = ['name']
    list_per_page = LIST_PER_PAGE


@admin.register(models.Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['value']
    search_fields = ['value']
    ordering = ['value']
    list_per_page = LIST_PER_PAGE

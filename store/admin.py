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


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ['name']
    prepopulated_fields = {"slug": ["name"]}
    list_per_page = LIST_PER_PAGE


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ['name']
    list_per_page = LIST_PER_PAGE


class VariationInline(admin.TabularInline):
    model = models.Variation
    list_display = ('color', 'size', 'quantity_in_stock')
    autocomplete_fields = ['color', 'size']
    extra = 0
    min_num = 1


class ProductTagInline(admin.TabularInline):
    model = models.ProductTag
    list_display = ['tag']
    autocomplete_fields = ['tag']
    extra = 0
    min_num = 1
    max_num = 12


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'unit_price', 'orderable')
    search_fields = ['name']
    autocomplete_fields = ['brand', 'category']
    prepopulated_fields = {"slug": ["name"]}
    inlines = [ProductTagInline, VariationInline]
    list_per_page = LIST_PER_PAGE


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('status', 'user', 'product', 'rating')
    autocomplete_fields = ['user', 'product']
    list_select_related = ['user', 'product']
    readonly_fields = ('user', 'product', 'rating', 'comment')
    list_per_page = LIST_PER_PAGE


@admin.register(models.Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('product', 'start_date', 'end_date', 'discount_rate')
    search_fields = ['product']
    autocomplete_fields = ['product']
    list_select_related = ['product']
    list_per_page = LIST_PER_PAGE


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ['products']
    list_per_page = LIST_PER_PAGE

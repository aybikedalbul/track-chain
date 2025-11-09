from django.contrib import admin

from .models import Product, ProductEvent


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "created_at")
    search_fields = ("name", "sku")


@admin.register(ProductEvent)
class ProductEventAdmin(admin.ModelAdmin):
    list_display = ("title", "product", "event_type", "occurred_at")
    list_filter = ("event_type", "occurred_at")
    search_fields = ("title", "product__name", "product__sku")
    autocomplete_fields = ("product",)

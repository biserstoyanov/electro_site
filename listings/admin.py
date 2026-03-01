# Register your models here.
from django.contrib import admin
from .models import Listing, Category


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "budget", "status", "created_at")
    list_filter = ("status", "city", "category")
    search_fields = ("title", "description", "city")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

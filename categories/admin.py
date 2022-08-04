from django.contrib import admin
from categories.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "subtitle",
    )
    list_filter = ("status",)
    search_fields = (
        "title",
        "content",
    )


admin.site.register(Category, CategoryAdmin)

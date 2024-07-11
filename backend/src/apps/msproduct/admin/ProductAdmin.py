from django.contrib import admin
from msproduct.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ["created"]
    search_fields = ["id", "title"]
    readonly_fields = ["id", "created", "modified"]
    list_display = (
        "id",
        "title",
        "description",
        "slug",
        "get_price",
        "created",
        "modified",
    )
    list_filter = ("created",)
    list_editable = ("title", "description")

    def get_price(self, obj):
        return obj.id

    get_price.admin_order_field = "price"
    get_price.short_description = "PRICE"

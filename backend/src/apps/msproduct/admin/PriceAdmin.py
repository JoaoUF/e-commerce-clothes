from django.contrib import admin
from msproduct.models import Price


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    ordering = ["created"]
    search_fields = ["id"]
    readonly_fields = ["id", "created", "modified"]
    list_display = (
        "id",
        "get_color",
        "get_size",
        "originalPrice",
        "discountPrice",
        "created",
        "modified",
    )
    list_filter = ("created",)
    list_editable = ("originalPrice", "discountPrice")

    def get_color(self, obj):
        return obj.id

    get_color.admin_order_field = "color"
    get_color.short_description = "COLOR"

    def get_size(self, obj):
        return obj.id

    get_size.admin_order_field = "size"
    get_size.short_description = "SIZE"

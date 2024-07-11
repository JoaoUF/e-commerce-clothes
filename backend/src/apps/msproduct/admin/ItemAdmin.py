from django.contrib import admin
from msproduct.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    ordering = ["created"]
    search_fields = ["id"]
    readonly_fields = [
        "id",
        "created",
        "modified",
        "status",
        "activate_date",
        "deactivate_date",
    ]
    list_display = ("id", "get_product", "get_bill", "quantity", "created", "modified")

    def get_product(self, obj):
        return obj.id

    get_product.admin_order_field = "product"
    get_product.short_description = "PRODUCT"

    def get_bill(self, obj):
        return obj.id

    get_bill.admin_order_field = "bill"
    get_bill.short_description = "BILL"

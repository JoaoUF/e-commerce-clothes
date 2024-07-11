from django.contrib import admin
from msproduct.models import ProductImage


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    search_fields = ["id"]
    readonly_fields = ["id"]
    list_display = ("id", "get_image", "get_product")

    def get_image(self, obj):
        return obj.id

    get_image.admin_order_field = "image"
    get_image.short_description = "IMAGE"

    def get_product(self, obj):
        return obj.id

    get_product.admin_order_field = "product"
    get_product.short_description = "PRODUCT"

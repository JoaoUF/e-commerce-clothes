from django.contrib import admin
from msproduct.models import Bill


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    ordering = ["modified"]
    search_fields = ["id", "user"]
    readonly_fields = ["id", "created", "modified"]
    list_display = ("id", "user", "total", "created", "modified")
    list_filter = ("modified",)

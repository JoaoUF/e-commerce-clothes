from django.contrib import admin
from msproduct.models import Color


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    ordering = ["created"]
    search_fields = ["id", "name"]
    readonly_fields = ["id", "created", "modified"]
    list_display = ("id", "name", "created", "modified")
    list_filter = ("created",)
    list_editable = ("name",)

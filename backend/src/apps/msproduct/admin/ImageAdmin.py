from django.contrib import admin
from msproduct.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ordering = ["created"]
    search_fields = ["id", "title"]
    readonly_fields = ["id", "created", "modified"]
    list_display = ("id", "title", "description", "slug", "created", "modified")
    list_filter = ("created",)
    list_editable = ("title", "description")

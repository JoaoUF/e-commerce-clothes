from django.contrib import admin
from msauthentication.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "last_login",
        "is_superuser",
        "first_name",
        "last_name",
        "created",
        "modified",
        "email",
        "is_verified",
        "is_active",
    )

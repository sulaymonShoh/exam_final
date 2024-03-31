from django.contrib import admin

from apps.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_deleted")
    search_fields = ("username",)
    date_hierarchy = "created_at"

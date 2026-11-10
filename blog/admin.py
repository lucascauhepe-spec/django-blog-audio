from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "status", "created_at"]
    list_filter = ["status", "created_at", "author"]
    search_fields = ["title", "content"]
    date_hierarchy = "created_at"
    readonly_fields = ["slug", "created_at", "updated_at"]
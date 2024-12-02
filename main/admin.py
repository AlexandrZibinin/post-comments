from django.contrib import admin
from django.utils.html import format_html

from main.models import Post


@admin.register(Post)
class LinkAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "text",
        "author",
        "created_at",
        "updated_at",
        "view_author_link",
    )
    list_filter = ["created_at"]

    def view_author_link(self, obj):
        return format_html(
            f'<a href="/admin/main/post/{obj.author.id}/change">Автор: {obj.author.username}</a>'
        )

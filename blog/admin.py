from django.contrib import admin
from .models import Post, Tag
from markdownx.admin import MarkdownxModelAdmin

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'preview', 'body', 'tags']


admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Tag)

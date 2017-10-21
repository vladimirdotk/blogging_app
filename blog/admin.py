from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    fields = ['created_date', 'title', 'slug', 'preview', 'body', 'tags']
    readonly_fields = ['created_date']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

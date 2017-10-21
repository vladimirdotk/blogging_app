from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'preview', 'body', 'tags']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

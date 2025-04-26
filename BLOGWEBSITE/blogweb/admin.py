from django.contrib import admin
from .models import BlogPosts



class BlogPostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'likes', 'comments')
    search_fields = ('title', 'author')
    list_filter = ('date',)
    ordering = ('-date',)


admin.site.register(BlogPosts, BlogPostsAdmin)
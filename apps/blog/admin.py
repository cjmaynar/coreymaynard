from django.contrib import admin

from models import Post, Comment, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'published')
    list_filter = ('date', 'categories', 'published')
    search_fields = ('title', 'body')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('approved', 'author', 'author_url', 'comment')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)

from django.contrib import admin
from blog.models    import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'date', 'published')
    list_filter   = ('date', 'categories', 'published')
    search_fields = ('title', 'body')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)

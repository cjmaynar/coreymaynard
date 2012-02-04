from django.contrib import admin
from portfolio.models import Project, Language

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'client', 'public')
    list_filter = ('completed', 'public')
    search_fields = ('title',)
    exclude = ('slug',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Language)

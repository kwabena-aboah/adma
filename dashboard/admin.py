from django.contrib import admin
from . models import Projects


class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'url', 'media', 'owner',)
	list_filter = ('name', 'media', 'owner',)
	search_fields = ('name', 'owner',)

admin.site.register(Projects, ProjectAdmin)
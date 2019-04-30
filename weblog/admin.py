from django.contrib import admin
from . models import Category, Entry


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'description',)
	list_filter = ('title',)
	search_fields = ('title',)
	prepopulated_fields = {'slug': ['title']}

admin.site.register(Category, CategoryAdmin)


class EntryAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'status', 'pub_date',)
	list_filter = ('status', 'pub_date', 'author',)
	search_fields = ('title', 'author',)
	raw_id_fields = ('author',)
	prepopulated_fields = {'slug': ['title']}
	ordering = ['status']

admin.site.register(Entry, EntryAdmin)

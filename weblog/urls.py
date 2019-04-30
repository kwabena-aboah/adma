from django.urls import path
from . import views
from . feeds import EntryFeed


app_name = 'weblog'
urlpatterns = [
    path('',views.index, name='index'),
    path('entries_index/', views.entries_index, name='entries_index'),
    path('weblog/<int:pk>/', views.entry_detail, name='entry_detail'),
    path('links/', views.links, name='links'),
    path('links_detail/<int:pk>/', views.links_detail, name='links_detail'),
    path('categories/', views.categories, name='categories'),
    path('categories/<slug:slug>/', views.category_detail, name='categories'),
    # new entries, links & categories
    path('new_entry/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:pk>/', views.edit_entry, name='edit_entry'),
    path('new_link/', views.new_link,  name='new_link'),
    path('edit_link/<int:pk>/', views.edit_link, name='edit_link'),
    path('new_category/', views.new_category, name='new_category'),
    path('edit_category/<slug:slug>/', views.edit_category, name='edit_category'),
    # delete entry, link or category
    path('delete_entry/<int:pk>/', views.delete_entry, name='delete_entry'),
    path('delete_link/<int:pk>/', views.delete_link, name='delete_link'),
    path('delete_category/<slug:slug>/',
         views.delete_category, name='delete_category'),
    # AdMA News Feed
    path('feed/', EntryFeed(), name='news_feed'),
]

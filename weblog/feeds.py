from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from . models import Entry


class EntryFeed(Feed):
	title = 'AdMA News Feed'
	link = '/weblog/'
	description = 'Our latest News'

	def items(self):
		return Entry.live.all()[:5]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return truncatewords(item.body, 20)
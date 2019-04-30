from django.contrib.sitemaps import Sitemap 
from . models import Entry


class EntrySitemap(Sitemap):
	changefreq = 'weekly'
	priority = 0.5

	def items(self):
		return Entry.live.all()

	def lastmod(self, item):
		return item.pub_date
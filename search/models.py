from django.db import models
# from django.contrib.flatpages.models import FlatPage 
from weblog.models import Entry


class SearchKeyword(models.Model):
	keyword = models.CharField(max_length=50)
	page = models.ForeignKey(Entry, on_delete=models.CASCADE)

	def __str__(self):
		return self.keyword
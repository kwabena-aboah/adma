from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
# from django.contrib.flatpages.models import FlatPage
from weblog.models import Entry
from . models import SearchKeyword 


def search(request):
	query = request.GET.get('q', '')
	keyword_results = results = []
	if query:
		keyword_results = Entry.objects.filter(searchkeyword__keyword__in=query.split()).distinct()
		if keyword_results.count() == 1:
			return HttpResponseRedirect(keyword_results[0].get_absolute_url())
		results = Entry.objects.filter(title__icontains=query)
	context = {'query':query,'keyword_results': keyword_results, 'results': results}
	return render(request, 'search/search.html', context)

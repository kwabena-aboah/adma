from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from . models import Entry, Category, Link
from . forms import EntryForm, CategoryForm, LinkForm
from dashboard.models import Projects

"""

Views for displaying all entries, categories, links and tags.
Details included.

"""
def index(request):
    entries = Entry.live.order_by('-pub_date')[0:6]
    media = Projects.objects.order_by('-name')[0:4]
    context = {'entries': entries, 'media':media}
    return render(request, 'weblog/index.html', context)


def entries_index(request):
    entry_list = Entry.live.order_by('-pub_date')
    category_list = Category.objects.all()

    paginator = Paginator(entry_list, 5)
    page = request.GET.get('page',1)
    try:
        entry = paginator.page(page)
    except PageNotAnInteger:
        entry = paginator.page(1)
    except EmptyPage:
        entry = paginator.page(paginator.num_pages)
    context = {'entry_list': entry_list, 'category_list': category_list, 'entry':entry}
    return render(request, 'weblog/entry_index.html', context)


def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    category_list = Category.objects.all()
    context = {'entry': entry, 'category_list': category_list}
    return render(request, 'weblog/entry_detail.html', context)


def links(request):
    link_list = Link.objects.all()
    paginator = Paginator(link_list, 5)
    page = request.GET.get('page',1)
    try:
        link = paginator.page(page)
    except PageNotAnInteger:
        link = paginator.page(1)
    except EmptyPage:
        link = paginator.page(paginator.num_pages)
    context = {'link_list': link_list, 'link': link}
    return render(request, 'weblog/link_list.html', context)


def links_detail(request, pk):
    link = get_object_or_404(Link, pk=pk)
    context = {'link': link}
    return render(request, 'weblog/links_detail.html', context)


def categories(request):
    category = Category.objects.all()
    paginator = Paginator(category, 5)
    page = request.GET.get('page', 1)
    try:
        cat = paginator.page(page)
    except PageNotAnInteger:
        cat = paginator.page(1)
    except EmptyPage:
        cat = paginator.page(paginator.num_pages)
    context = {'category': category, 'cat': cat}
    return render(request, 'weblog/category.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    object_list = category.entry_set.all()
    context = {'category': category, 'object_list': object_list}
    return render(request, 'weblog/category_detail.html', context)

"""

Views of new category, link, tags, and entry. Editing inclusive

"""


@login_required
def new_entry(request):
    if request.method != 'POST':
        forms = EntryForm()
    else:
        forms = EntryForm(request.POST, request.FILES)
        if forms.is_valid():
            new_entry = forms.save(commit=False)
            new_entry.author = request.user
            new_entry.save()
            messages.info(request, "Entry Successfully added")
            return HttpResponseRedirect(reverse('weblog:entries_index'))
    context = {'forms': forms}
    return render(request, 'theweb/new_entry.html', context)


@login_required
def edit_entry(request, pk):
    entry = Entry.objects.get(pk=pk)
    if request.method != 'POST':
        forms = EntryForm(instance=entry)
    else:
        forms = EntryForm(instance=entry, data=request.POST)
        if forms.is_valid():
            forms.save()
            messages.info(request, "Changes Successfully saved")
            return HttpResponseRedirect(reverse('weblog:entry_detail', args=[entry.pk]))
    context = {'entry': entry, 'forms': forms}
    return render(request, 'theweb/edit_entry.html', context)


@login_required
def new_link(request):
    if request.method != 'POST':
        forms = LinkForm()
    else:
        forms = LinkForm(request.POST)
        if forms.is_valid():
            new_link = forms.save(commit=False)
            new_link.posted_by = request.user
            new_link.save()
            messages.info(request, "Link Successfully Added")
            return HttpResponseRedirect(reverse('weblog:links'))
    context = {'forms': forms}
    return render(request, 'theweb/new_link.html', context)


@login_required
def edit_link(request, pk):
    link = Link.objects.get(pk=pk)
    if request.method != 'POST':
        forms = LinkForm(instance=link)
    else:
        forms = LinkForm(instance=link, data=request.POST)
        if forms.is_valid():
            forms.save()
            messages.info(request, "Changes Successfully saved")
            return HttpResponseRedirect(reverse('weblog:links_detail', args=[link.pk]))
    context = {'link': link, 'forms': forms}
    return render(request, 'theweb/edit_link.html', context)


@login_required
def new_category(request):
    if request.method != 'POST':
        forms = CategoryForm()
    else:
        forms = CategoryForm(request.POST)
        if forms.is_valid():
            new_category = forms.save(commit=False)
            new_category.save()
            messages.info(request, "Category Successfully Added")
            return HttpResponseRedirect(reverse('weblog:categories'))
    context = {'forms': forms}
    return render(request, 'theweb/new_category.html', context)


@login_required
def edit_category(request, slug):
    category = Category.objects.get(slug=slug)
    if request.method != 'POST':
        forms = CategoryForm(instance=category)
    else:
        forms = CategoryForm(instance=category, data=request.POST)
        if forms.is_valid():
            forms.save()
            messages.info(request, "Changes Successfully saved")
            return HttpResponseRedirect(reverse('weblog:categories', args=[category.slug]))
    context = {'category': category, 'forms': forms}
    return render(request, 'theweb/edit_category.html', context)


"""

Views display delete entry, delete links and delete categories

"""


@login_required
def delete_entry(request, pk):
    entry = Entry.objects.get(pk=pk)
    if entry.author != request.user:
        raise Http404
    if entry:
        entry.delete()
        messages.info(request, "Entry Deleted")
        return HttpResponseRedirect(reverse('weblog:entries_index'))
    return render(request, 'weblog/entry_index.html')


@login_required
def delete_link(request, pk):
    link = Link.objects.get(pk=pk)
    if link.posted_by != request.user:
        raise Http404
    if link:
        link.delete()
        messages.info(request, "Link Deleted")
        return HttpResponseRedirect(reverse('weblog:links'))
    return render(request, 'weblog/link_list.html')


@login_required
def delete_category(request, slug):
    category = Category.objects.get(slug=slug)
    if category:
        category.delete()
        messages.info(request, "Category Deleted")
        return HttpResponseRedirect(reverse('weblog:categories'))
    return render(request, 'weblog/category.html')

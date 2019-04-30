from django import forms
from .models import Entry, Category, Link


class EntryForm(forms.ModelForm):
    body = forms.CharField(
            label = 'Body',
            widget = forms.TextInput(
                attrs = {'class': 'materialize-textarea', 'name': 'body'}
            ) 
        )
    excerpt = forms.CharField(
            label = 'Excerpt',
            widget = forms.TextInput(
                attrs = {'class': 'materialize-textarea', 'name': 'excerpt'}
            )
        )

    class Meta:
        model = Entry
        fields = (
            'title', 'excerpt', 'body', 'cover_pic', 
            'pub_date', 'author', 'status', 'categories', 'tags',
        )
        labels = {'text': ''}
        


class CategoryForm(forms.ModelForm):
    description = forms.CharField(
        label = 'Description',
        widget = forms.TextInput(
            attrs = {'class': 'materialize-textarea', 'name':'description'}
            )
        )
    class Meta:
        model = Category
        fields = (
            'title', 'description',
        )
        labels = {'text': ''}


class LinkForm(forms.ModelForm):
    description = forms.CharField(
        label = 'Description',
        widget = forms.TextInput(
            attrs = {'class': 'materialize-textarea', 'name': 'description'}
            )
        )
    description_html = forms.CharField(
        label = 'Description html',
        widget = forms.TextInput(
            attrs = {'class': 'materialize-textarea', 'name': 'description_html'}
            )
        )
    class Meta:
        model = Link
        fields = (
            'title', 'description', 'description_html', 'url', 'via_name', 'via_url',
            'posted_by', 'pub_date', 'tags',
        )
        labels = {'text': ''}
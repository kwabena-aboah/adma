import datetime

from django.db import models
from django.contrib.auth.models import User

from markdown import markdown
from tagging.fields import TagField


class Category(models.Model):
    title = models.CharField(
        max_length=250, help_text='Maximum 250 characters.')
    slug = models.SlugField(
        unique=True, help_text="Suggested value automatically generated from title. Must be unique")
    description = models.TextField()

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s" % self.slug


class MyModel(models.Model):
    name = models.CharField(max_length=50)
    object_fetcher = models.Manager()

LIVE_STATUS = 1
DRAFT_STATUS = 2
HIDDEN_STATUS = 3
STATUS_CHOICES = (
    (LIVE_STATUS, 'Live'),
    (DRAFT_STATUS, 'Draft'),
)


class LiveEntryManager(models.Manager):

    def get_query_set(self):
        return super(LiveEntryManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)


class Entry(models.Model):
    title = models.CharField(
        max_length=250, help_text="Maximum 250 characters.")
    slug = models.SlugField(unique_for_date='pub_date',
                            help_text="Suggested value automatically generated from title. Must be unique.")
    excerpt = models.TextField(
        blank=True, help_text="A short summary of the entry. Optional.")
    body = models.TextField()
    cover_pic = models.FileField(upload_to="Uploads/entries", blank=False,
                                 null=False, help_text='Cover image for entry.')
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS,
                                 help_text="Only entries with live status will be publicly displayed.")
    categories = models.ManyToManyField(Category)
    excerpt_html = models.TextField(editable=False, blank=True, max_length=20)
    body_html = models.TextField(editable=False, blank=True)
    tags = TagField(help_text="Separate tags with spaces.")
    live = LiveEntryManager()
    objects = models.Manager()

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save(force_insert, force_update)

    def get_absolute_url(self):
        return "/weblog/%s/" % self.pk


class Link(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(
        blank=True, help_text='A brief description of the URL/Link. Optional.')
    description_html = models.TextField(
        editable=True, blank=True, help_text='A brief description of the URL/Link. Optional.')
    url = models.URLField('URL', unique=True)
    via_name = models.CharField('Via', max_length=250, blank=True,
                                help_text='The name of the person whose site you spotted the link on. Optional.')
    via_url = models.URLField(
        'Via URL', blank=True, help_text='The URL of the site where you spotted the link. Optional.')
    enable_comments = models.BooleanField(default=True)
    post_elsewWhere = models.BooleanField(
        'Post to admagovgh.herokuapp.com', default=True, help_text='If checked, this link will be posted both to your weblog.')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date',
                            help_text='Must be unique for the publication date.')
    tags = TagField()

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return (self.id, self.post_elsewWhere)
        # import pydelicious
        # pydelicious.add(settings.DELICIOUS_USER,
        # 				settings.DELICIOUS_PASSWORD,
        # 				smart_str(self.url),
        # 				smart_str(self.title),
        # 				smart_str(self.tags))
        # if self.description:
        # 	self.description_html = markdown(self.description)
        # super(Link,self).save()

    def get_absolute_url(self):
        return '/links_detail/%s' % self.id

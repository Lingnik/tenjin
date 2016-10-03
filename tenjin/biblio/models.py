from django.db import models
from django.db.models import Sum
from django.utils import timezone


class Content(models.Model):
    title = models.CharField(max_length=1000)
    content_type = models.CharField(max_length=50)
    authors = models.ManyToManyField('biblio.Author')
    created_date = models.DateTimeField(default=timezone.now)

    cites = models.ManyToManyField('biblio.Content', blank=True)
    publication = models.ForeignKey('biblio.Publication', blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=2083, blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)

    cited_by_scholar = models.IntegerField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)

    def taylor_cites(self):
        this_id = self.id
        if Content.objects.get(id=6).cites.filter(id=this_id).exists():
            return True
        return ""

    def author_list(self):
        return '; '.join([str(a) for a in self.authors.all()])
    author_list.admin_order_field = 'authors'

    def published_date_str(self):
        return self.published_date.strftime("%Y-%m-%d") if self.published_date else None
    published_date_str.admin_order_field = 'published_date'
    published_date_str.short_description = 'Published Date'

    def __str__(self):
        return '[{}] {} ({})'.format(
            self.id,
            self.title,
            self.authors.first()
        )


class Author(models.Model):
    given_name = models.CharField(max_length=200, blank=True, null=True)
    family_name = models.CharField(max_length=200)
    url = models.URLField(max_length=2083, blank=True, null=True)

    def cited_by_scholar(self):
        return self.content_set.all().aggregate(Sum('cited_by_scholar'))['cited_by_scholar__sum']

    def name(self):
        return "{}, {}".format(self.family_name, self.given_name)
    name.admin_order_field = ('family_name', 'given_name')

    def __str__(self):
        return self.name()


class Degree(models.Model):
    author = models.ForeignKey('biblio.Author', blank=True, null=True)

    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    organization = models.ForeignKey('biblio.Organization', blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.organization:
            return '{}, {} ({})'.format(self.degree, self.major, self.organization)
        return '{}, {}'.format(self.degree, self.major)


class Position(models.Model):
    author = models.ForeignKey('biblio.Author', blank=True, null=True)

    name = models.CharField(max_length=100)
    organization = models.ForeignKey('biblio.Organization', blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.organization:
            return '{} ({})'.format(self.name, self.organization)
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Publication(models.Model):
    name = models.CharField(max_length=1000)
    editors = models.ManyToManyField('biblio.Author', blank=True, null=True)

    def __str__(self):
        return self.name

from django.contrib import admin

from .models import Content, Author, Publication, Position, Organization, Degree


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'author_list', 'published_date_str', 'cited_by_scholar', 'taylor_cites')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'organization', 'start_date', 'end_date')
    ordering = ('author', 'start_date', 'end_date', 'name', 'organization')


class PositionInline(admin.TabularInline):
    model = Position


class ContentInline(admin.TabularInline):
    model = Author.content_set.through


class DegreeInline(admin.TabularInline):
    model = Degree


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'cited_by_scholar']

    inlines = [
        ContentInline,
        PositionInline,
        DegreeInline
    ]

admin.site.register(Publication)
admin.site.register(Organization)

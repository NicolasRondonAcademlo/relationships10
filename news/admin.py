from django.contrib import admin
from .models import Reporter, Article

# Register your models here.
#admin.site.register(Reporter)
#admin.site.register(Article)


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Article',  {'fields': ['headline', 'content', 'pub_date']}),
        ('Reporter', {'fields': ['reporter']}),
        ]
    list_display = ('pub_date', 'reporter', 'headline')
    date_hierarchy = 'pub_date'
    list_editable = ('headline',)
    list_display_links = ( 'reporter',)
    ordering = ('-pub_date',)
    search_fields = ['headline', 'content']

@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Algo",  {'fields': ['first_name', 'last_name', 'email']}),
        ]
    list_display = ('first_name', 'last_name', 'email')

admin.site.register(Article, ArticleAdmin)
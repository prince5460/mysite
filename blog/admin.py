from django.contrib import admin

# Register your models here.
from .models import BlogArticle


class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')
    search_fields = ('title', 'article')
    list_filter = ('publish', 'author')


admin.site.register(BlogArticle, BlogArticleAdmin)

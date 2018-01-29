from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class BlogArticle(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    article = models.TextField(verbose_name='文章')
    CHOICE_TAG = (
        ('tech', 'Tech'),
        ('life', 'Life'),
        ('news', 'News'),
    )
    tag = models.CharField(max_length=10, default='', choices=CHOICE_TAG, verbose_name='标签')
    publish = models.DateTimeField(default=timezone.now, verbose_name='时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ('-publish',)

    def __str__(self):
        return self.title

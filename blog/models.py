from django.db import models
from django.utils.timezone import datetime


class Tag(models.Model):
    """
    Blog Tag
    """
    name = models.CharField(max_length=128, verbose_name='тег')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Post(models.Model):
    """
    Blog Posts
    """
    title = models.CharField('заголовок', max_length=256)
    slug = models.SlugField('url')
    preview = models.TextField('предпросмотр')
    body = models.TextField('заметка')
    created_date = models.DateTimeField(
        null=False, blank=False, verbose_name='дата создания', default=datetime.now()
    )
    tags = models.ManyToManyField(Tag, verbose_name='тэг')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
        ordering = ('-created_date',)

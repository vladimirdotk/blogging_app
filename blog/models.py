from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from markdownx.models import MarkdownxField


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
    slug = AutoSlugField(
        populate_from='title',
        unique_with='created_date'
    )
    preview = MarkdownxField('предпросмотр')
    body = MarkdownxField('заметка')
    created_date = models.DateTimeField(
        null=False, blank=False, verbose_name='дата создания', auto_now_add=True
    )
    tags = models.ManyToManyField(Tag, verbose_name='тэг')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})


    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
        ordering = ('-created_date',)

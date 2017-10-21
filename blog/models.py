from django.db import models


class Post(models.Model):
    """
    Blog Posts
    """
    title = models.CharField(max_length=256, verbose_name='заголовок')
    slug = models.SlugField(verbose_name='Url')
    body = models.TextField(verbose_name='заметка')
    created_date = models.DateTimeField(auto_created=True, verbose_name='дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'

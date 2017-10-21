from django.db import models


class Post(models.Model):
    """
    Blog Posts
    """
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    body = models.TextField()
    created_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'

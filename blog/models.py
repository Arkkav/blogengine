from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    # it's could be done in the Tag class, but it looks like The Post class is main in this case
    date_pub = models.DateTimeField(auto_now_add=True)  # to save current date when the field saved to DB
    # auto_now to save current date when a model is changed

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})  # no "url" func. and "slug" arg in pattern

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

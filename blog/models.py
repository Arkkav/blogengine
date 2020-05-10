from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time  # number of seconds from 01.01.1970


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    # it's could be done in the Tag class, but it looks like The Post class is main in this case
    date_pub = models.DateTimeField(auto_now_add=True)  # to save current date when the field saved to DB
    # auto_now to save current date when a model is changed

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})  # no "url" func. and "slug" arg in pattern

    def get_update_url(self):  # just call this method in patten instead of passing arg 'slug'
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

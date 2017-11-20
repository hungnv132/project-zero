from django.db import models
from core.models import TrackingTime, TrackingUser
from slugify import slugify
from core.constants import ARTICLE_STATUS


class Category(TrackingTime):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def save(self, **kwargs):
        if self.name:
            self.slug = slugify(self.name, only_ascii=True)
        return super(Category, self).save(**kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(TrackingTime, TrackingUser):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(Category, related_name='articles',
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True)
    content = models.TextField()
    status = models.SmallIntegerField(choices=ARTICLE_STATUS, default=ARTICLE_STATUS[0][0])

    def save(self, **kwargs):
        if self.title:
            self.slug = slugify(self.title, only_ascii=True)
        return super(Article, self).save(**kwargs)

from django.db import models
from django.core.urlresolvers import reverse
from slugify import slugify
from cms.models.pluginmodel import CMSPlugin
from core.models import TrackingTime, TrackingUser
from core.constants import PAGE_STATUS
from taggit.managers import TaggableManager


class CommonModel(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)

    def save(self, **kwargs):
        if self.title:
            self.slug = slugify(self.title, only_ascii=True)
        return super(CommonModel, self).save(**kwargs)

    class Meta:
        abstract = True


class Category(CommonModel, TrackingTime, TrackingUser):

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(CommonModel, TrackingTime, TrackingUser):
    intro = models.TextField(blank=True, null=True)
    content = models.TextField()
    status = models.SmallIntegerField(choices=PAGE_STATUS, default=PAGE_STATUS[0][0])
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.SET_NULL,
                                 blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnail/%Y_%m_%d', blank=True, null=True)

    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail_view', args=(self.slug, self.id))

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class RecentPosts(CMSPlugin):
    recent_posts_number = models.SmallIntegerField(default=5)
from django.core.paginator import Paginator
from django.db.models import Count
from taggit.models import TaggedItem
from blog.models import Post
from blog.utils import rename_object


def get_all_posts(post_status=2):
    """
    :param post_status: status of post: Published or Draft. Default is published.
    :return: List of Posts
    """
    return Post.objects.filter(status=post_status).order_by('-id')


def _build_paginator(posts, page_number, posts_per_page):
    paginator = Paginator(posts, posts_per_page)
    return paginator.page(page_number)


def get_posts_by_page(page_number=1, posts_per_page=5, post_status=2):
    """
    :param page_number: the page number needs query, default is the first page.
    :param posts_per_page: number of posts will display on one page. Default is 5 posts.
    :param post_status: status of post: published or draft. Default is published.
    :return: list of posts by page number
    """
    all_posts = get_all_posts(post_status)
    return _build_paginator(all_posts, page_number=1, posts_per_page=5)


def find_posts(**params):
    posts = get_all_posts()
    if params['q']:
        # Find posts by search keyword.
        posts = posts.filter(title__contains=params['q'])
    if params['tag']:
        # Find posts by tag's slug.
        posts = posts.filter(tags__slug=params['tag'])
    page_number = params['page_number'] or 1
    posts_per_page = params['posts_per_page'] or 5
    return _build_paginator(posts, page_number, posts_per_page)


def get_recent_posts(post_number):
    """
    :param post_number: the number of posts need to retrieve
    :return: list of posts
    """
    return get_all_posts()[:post_number]


def get_popular_tags(top=10):
    """
    Get a list of popular tags
    """
    result = TaggedItem.objects\
        .values('tag__name', 'tag__slug')\
        .annotate(count=Count('tag__slug'))\
        .order_by('-count', 'tag__name')
    return rename_object(result[:top])


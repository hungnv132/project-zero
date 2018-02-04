from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from taggit.models import Tag, TaggedItem
from core.utils import is_integer
from blog.models import RecentPosts
from blog.services import find_posts, get_recent_posts, get_popular_tags

POSTS_PER_PAGE = 3


@plugin_pool.register_plugin
class PublishedPostList(CMSPluginBase):
    model = CMSPlugin
    name = _('Published Post List')
    render_template = 'blog/plugins/published_posts.html'
    cache = False

    def render(self, context, instance, placeholder):
        request = context.get('request', None)
        context = super(PublishedPostList, self).render(context, instance, placeholder)

        page_number = request.GET.get('page', 1)
        if not is_integer(page_number):
            page_number = 1

        params = {
            'q': request.GET.get('q', None),
            'tag': request.GET.get('tag', None),
            'page_number': page_number,
            'posts_per_page': POSTS_PER_PAGE,
        }
        context['posts'] = find_posts(**params)
        context['current_page_number'] = page_number
        context.update(params)
        return context


@plugin_pool.register_plugin
class RecentPostsPlugin(CMSPluginBase):
    model = RecentPosts
    name = _('Recent Posts')
    render_template = 'blog/plugins/recent_posts.html'
    cache = False

    def render(self, context, instance, placeholder):
        context = super(RecentPostsPlugin, self).render(context, instance, placeholder)
        context['recent_posts'] = get_recent_posts(instance.recent_posts_number)
        return context


@plugin_pool.register_plugin
class SearchPostsPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _('Search Posts')
    render_template = 'blog/plugins/search_posts.html'
    cache = False

    def render(self, context, instance, placeholder):
        context = super(SearchPostsPlugin, self).render(context, instance, placeholder)
        return context


@plugin_pool.register_plugin
class PopularTagsPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _('Popular Tags')
    render_template = 'blog/plugins/popular_tags.html'
    cache = True

    def render(self, context, instance, placeholder):
        context = super(PopularTagsPlugin, self).render(context, instance, placeholder)
        context['popular_tags'] = get_popular_tags(top=10)
        return context

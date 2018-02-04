from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class BlogApphook(CMSApp):
    name = 'Blog Apphook'
    app_name = 'blog'

    def get_urls(self, page=None, language=None, **kwargs):
        return ['blog.urls']

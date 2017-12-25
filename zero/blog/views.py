from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from blog.models import Post

POST_PER_PAGE = 4


class Homepage(TemplateView):
    template_name = 'blog/home_page.html'

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        page_number = kwargs.get('page_number', 1)
        posts = Post.objects.filter(status=2).order_by('-id')
        paginator = Paginator(posts, POST_PER_PAGE)
        context['posts'] = paginator.page(page_number)
        context['current_page_number'] = int(page_number)
        return context


class AboutMe(TemplateView):
    template_name = 'blog/about_me.html'


class PostDetail(TemplateView):
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        slug = kwargs.get('slug', None)
        id = kwargs.get('id', None)
        post = get_object_or_404(Post, slug=slug, pk=id, status=2)
        context['post'] = post
        return context

    def get(self, request, *args, **kwargs):
        return super(PostDetail, self).get(request, *args, **kwargs)


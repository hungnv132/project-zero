from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.http import Http404
from blog.models import Post


class Homepage(TemplateView):
    template_name = 'blog/home_page.html'

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        posts = Post.objects.filter(status=2).order_by('-id')
        context['posts'] = posts
        return context


class AboutMe(TemplateView):
    template_name = 'blog/about_me.html'


class PostDetail(TemplateView):
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        slug = kwargs.get('slug', None)
        id = kwargs.get('id', None)
        post = Post.objects.get(slug=slug, pk=id)
        context['post'] = post
        return context

    def get(self, request, *args, **kwargs):
        return super(PostDetail, self).get(request, *args, **kwargs)


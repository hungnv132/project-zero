from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from blog.models import Post


class PostListView(TemplateView):
    template_name = 'blog/post_list.html'


class PostDetailView(TemplateView):
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        slug = kwargs.get('slug', None)
        id = kwargs.get('id', None)
        post = get_object_or_404(Post, slug=slug, pk=id, status=2)
        context['post'] = post
        context['post_tags'] = post.tags.all()
        return context

    def get(self, request, *args, **kwargs):
        return super(PostDetailView, self).get(request, *args, **kwargs)


from blog.models import Post


def global_context(request):
    context = dict()
    recently_posts = Post.objects.filter(status=2).order_by('-id')[:5]
    context['recently_posts'] = recently_posts
    return context

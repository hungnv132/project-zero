from django.conf.urls import url
from blog.views import PostListView, PostDetailView

urlpatterns = [
    url(r'^$', view=PostListView.as_view(), name='post_list_view'),
    url(r'^(?P<slug>[0-9a-zA-Z\-_]+)-(?P<id>[0-9]+).html$', view=PostDetailView.as_view(),
        name='post_detail_view'),
]
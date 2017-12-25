from django.conf.urls import url, include
from blog.views import Homepage, AboutMe, PostDetail

urlpatterns = [
    url(r'^$', view=Homepage.as_view(), name='home_page'),
    url(r'^page/(?P<page_number>[0-9]+)', view=Homepage.as_view(), name='home_page'),
    url(r'^me.html$', view=AboutMe.as_view(), name='about_me'),
    url(r'^(?P<slug>[0-9a-zA-Z\-_]+)-(?P<id>[0-9]+).html$', view=PostDetail.as_view(),
        name='post_detail')

]
from django.conf.urls import url
from blogme.views import Home


urlpatterns = [
    url(r'', view=Home.as_view(), name='home_page')
]
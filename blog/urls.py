from blog.views import PostList, PostDetail
from django.conf.urls import url

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post-list'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetail.as_view(), name='post-detail'),
]

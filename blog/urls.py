from blog.views import PostList, PostDetail
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<slug>', PostDetail.as_view(), name='post-detail'),
]

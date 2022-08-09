from blogs.views import PostList, PostDetail
from django.urls import path

app_name = "blogs"


urlpatterns = [
    path("list/", PostList.as_view(), name="home"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="index"),
]

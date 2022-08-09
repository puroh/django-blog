from blogs.views import PostList, PostDetail, IndexView
from django.urls import path

app_name = "blogs"


urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
]

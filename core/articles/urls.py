from django.urls import path
from .views import (
    # ARTICLE
    MyArticleView,
    ArchiveArticleView,
    ListArticleView,
    CreateArticleView,
    UpdateArticleView,
    DeleteArticleView,
    DetailArticleView,
    ShareArticleView,
    # TAGS
    ListArticleTag,
    CreateArticleTag,
    UpdateArticleTag,
    DeleteArticleTag,
)

app_name = "article"

urlpatterns = [
    # ARTICLE
    path("list/", ListArticleView.as_view(), name="list"),
    path("my_list/", MyArticleView.as_view(), name="my_list"),
    path("archive/", ArchiveArticleView.as_view(), name="archive"),
    path("create/", CreateArticleView.as_view(), name="create"),
    path("update/<int:pk>/", UpdateArticleView.as_view(), name="update"),
    path("detail/<int:pk>/", DetailArticleView.as_view(), name="detail"),
    path("delete/<int:pk>/", DeleteArticleView.as_view(), name="delete"),
    # SHARED
    path("share_detail/<int:pk>/", ShareArticleView.as_view(), name="share_detail"),
    # TAGS
    path("tag_list/", ListArticleTag.as_view(), name="tag_list"),
    path("tag_create/", CreateArticleTag.as_view(), name="tag_create"),
    path("tag_update/<int:pk>/", UpdateArticleTag.as_view(), name="tag_update"),
    path("tag_delete/<int:pk>/", DeleteArticleTag.as_view(), name="tag_delete"),
]

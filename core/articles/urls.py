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
    #SHARED
    ShareArticleDetailView,
    AddCommentView,
    SentArticleListView,
    SentArticleView,
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
    path("sent/", SentArticleListView.as_view(), name="sent"),
    path("share_detail/<int:pk>/", ShareArticleDetailView.as_view(), name="share_detail"),
    path("comment/<int:article_id>/", AddCommentView.as_view(), name="comment"),
    path('post/<int:article_id>/',SentArticleView.as_view(), name = 'post'),
    # TAGS
    path("tag_list/", ListArticleTag.as_view(), name="tag_list"),
    path("tag_create/", CreateArticleTag.as_view(), name="tag_create"),
    path("tag_update/<int:pk>/", UpdateArticleTag.as_view(), name="tag_update"),
    path("tag_delete/<int:pk>/", DeleteArticleTag.as_view(), name="tag_delete"),
]

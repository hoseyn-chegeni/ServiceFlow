from django.urls import path
from .views import MyArticleView,ArchiveArticleView,ListArticleView,CreateArticleView,UpdateArticleView,DeleteArticleView,DetailArticleView

app_name = 'article'

urlpatterns = [
        path('list/',ListArticleView.as_view(),name = 'list') ,
        path('my_list/',MyArticleView.as_view(),name = 'my_list') ,
        path('archive/',ArchiveArticleView.as_view(),name = 'archive') ,
        path('create/',CreateArticleView.as_view(),name = 'create') ,
        path('update<int:pk>/',UpdateArticleView.as_view(),name = 'update') ,
        path('detail/<int:pk>/',DetailArticleView.as_view(),name = 'detail') ,
        path('delete/<int:pk>/',DeleteArticleView.as_view(),name = 'delete') ,
]
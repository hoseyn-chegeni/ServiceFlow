import django_filters
from django_filters import FilterSet
from .models import Article, ArticleTags


class ArticleFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "tags",
            "author",
            "related_articles",
        ]


class ArticleTagFilter(FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = ArticleTags
        fields = [
            "id",
            "name",
        ]

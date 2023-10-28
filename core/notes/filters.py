import django_filters
from django_filters import FilterSet
from .models import Note


class NoteFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Note
        fields = [
            "id",
            "title",
            "author",
            "is_public",
            "author",
            "tags",
        ]


class PublicNoteFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Note
        fields = [
            "id",
            "title",
            "author",
            "author",
            "tags",
        ]

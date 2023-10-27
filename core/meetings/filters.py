import django_filters
from django_filters import FilterSet
from . models import Meetings


class InvitedMeetingsFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Meetings
        fields = ['id','title','location', 'organizer', 'status']


class MyCreatedMeetingsFilter(FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Meetings
        fields = ['id','title','location','status']
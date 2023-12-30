from django.urls import path
from .views import FlowCreateView,FlowDeleteView,FlowDetailView,FlowListView,FlowUpdateView,StateCreateView,StateDeleteView,StateListView,StateDetailView,StateUpdateView

app_name = 'flow' 

urlpatterns = [
    #FLOW
    path('list/', FlowListView.as_view(),name='list'),
    path('create/', FlowCreateView.as_view(),name='create'),
    path('detail/<int:pk>/', FlowDetailView.as_view(),name='detail'),
    path('update/<int:pk>/', FlowUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/', FlowDeleteView.as_view(),name='delete'),
    #STATE
    path('state/list/', StateListView.as_view(),name='state_list'),
    path('state/create/', StateCreateView.as_view(),name='state_create'),
    path('state/detail/<int:pk>/', StateDetailView.as_view(),name='state_detail'),
    path('state/update/<int:pk>/', StateUpdateView.as_view(),name='state_update'),
    path('state/delete/<int:pk>/', StateDeleteView.as_view(),name='state_delete'),
]

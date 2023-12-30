from django.urls import path
from .views import FlowCreateView,FlowDeleteView,FlowDetailView,FlowListView,FlowUpdateView

app_name = 'flow' 

urlpatterns = [
    path('list/', FlowListView.as_view(),name='list'),
    path('create/', FlowCreateView.as_view(),name='create'),
    path('detail/<int:pk>/', FlowDetailView.as_view(),name='detail'),
    path('update/<int:pk>/', FlowUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/', FlowDeleteView.as_view(),name='delete'),

]

from django.urls import path
from .views import DepartmentDeleteView, DepartmentUpdateView,DepartmentCreateView,DepartmentDetailView,DepartmentListView

app_name = 'department'

urlpatterns = [
    path('list/',DepartmentListView.as_view(),name='list'),
    path('create/',DepartmentCreateView.as_view(),name='create'),
    path('detail/<int:pk>/',DepartmentDetailView.as_view(),name='detail'),
    path('update/<int:pk>/',DepartmentUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',DepartmentDeleteView.as_view(),name='delete'),
]
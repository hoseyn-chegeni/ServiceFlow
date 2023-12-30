from django.shortcuts import render
from base.views import BaseCreateView,BaseDeleteView,BaseDetailView,BaseListView,BaseUpdateView
from .models import WorkFlow
from .filters import FlowFilters
from django.urls import reverse_lazy


# Create your views here.
class FlowListView(BaseListView):
    model = WorkFlow
    template_name = 'flow/list.html'
    filterset_class = FlowFilters
    context_object_name = 'flow'
    permission_required = 'flow.view_workflow'



class FlowCreateView(BaseCreateView):
    model = WorkFlow
    template_name = 'flow/create.html'
    fields = ['name','root','diagram','is_active',]
    permission_required = 'flow.add_workflow'
    success_message = 'Flow Successfully Added'
    url = 'flow:detail'


class FlowDetailView(BaseDetailView):
    model = WorkFlow
    template_name = 'flow/detail.html'
    permission_required = 'flow.view_workflow'
    context_object_name = 'flow'


class FlowUpdateView(BaseUpdateView):
    model = WorkFlow
    template_name = 'flow/update.html'
    permission_required = 'flow.change_workflow'
    context_object_name = 'flow'
    url = 'flow:detail'
    fields = ['name','root','diagram','is_active',]


class FlowDeleteView(BaseDeleteView):
    model = WorkFlow
    template_name = 'flow/delete.html'
    permission_required = 'flow.delete_workflow'
    success_url = reverse_lazy('flow:list')
    message = 'Flow Successfully Deleted.'
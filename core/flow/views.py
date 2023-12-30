from django.shortcuts import render
from base.views import BaseCreateView,BaseDeleteView,BaseDetailView,BaseListView,BaseUpdateView
from .models import WorkFlow, State
from .filters import FlowFilters, StateFilters
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
    success_message = 'Flow Successfully Updated'


class FlowDeleteView(BaseDeleteView):
    model = WorkFlow
    template_name = 'flow/delete.html'
    permission_required = 'flow.delete_workflow'
    success_url = reverse_lazy('flow:list')
    message = 'Flow Successfully Deleted.'




#STATE
#STATE
#STATE
#STATE
#STATE
    
class StateListView(BaseListView):
    model = State
    template_name = 'flow/state/list.html'
    filterset_class = StateFilters
    context_object_name = 'state'
    permission_required = 'flow.view_state'



class StateCreateView(BaseCreateView):
    model = State
    template_name = 'flow/state/create.html'
    fields = ['state','team','process_percentage','action','is_active']
    permission_required = 'flow.add_state'
    success_message = 'State Successfully Added'
    url = 'flow:state_detail'


class StateDetailView(BaseDetailView):
    model = State
    template_name = 'flow/state/detail.html'
    permission_required = 'flow.view_state'
    context_object_name = 'state'


class StateUpdateView(BaseUpdateView):
    model = State
    template_name = 'flow/state/update.html'
    permission_required = 'flow.change_state'
    context_object_name = 'state'
    url = 'flow:state_detail'
    fields = ['state','team','process_percentage','action','is_active']
    success_message = 'State Successfully Updated'


class StateDeleteView(BaseDeleteView):
    model = State
    template_name = 'flow/state/delete.html'
    permission_required = 'flow.delete_state'
    success_url = reverse_lazy('flow:state_list')
    message = 'State Successfully Deleted'


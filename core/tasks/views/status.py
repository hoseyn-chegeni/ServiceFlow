from django.views.generic import ListView,CreateView, DetailView,UpdateView,DeleteView
from ..models import TaskStatus
from django.urls import reverse_lazy
from ..forms import CreateTaskStatusForm

class StatusListView(ListView):
    model = TaskStatus
    context_object_name = "status"
    template_name = "tasks/status/list.html"


class StatusDetailView(DetailView):
    model = TaskStatus
    template_name = "tasks/status/detail.html"
    context_object_name = 'status'


class StatusCreateView(CreateView):
    template_name = "tasks/status/create.html"
    form_class = CreateTaskStatusForm


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self) :
        return reverse_lazy('tasks:detail_status', kwargs={'pk': self.object.pk})
    

class StatusUpdateView(UpdateView):
    model = TaskStatus
    fields = ('name','description', 'is_active')
    template_name = "tasks/status/update.html"

    def get_success_url(self) :
        return reverse_lazy('tasks:detail_status', kwargs={'pk': self.object.pk})


class StatusDeleteView(DeleteView):
    model = TaskStatus
    template_name = "tasks/status/delete.html"
    success_url = reverse_lazy("tasks:list_status")


from django.views.generic import ListView,CreateView, DetailView,UpdateView,DeleteView
from ..models import TaskType
from django.urls import reverse_lazy
from ..forms import CreateTaskTypeForm

class TypeListView(ListView):
    model = TaskType
    context_object_name = "type"
    template_name = "tasks/type/list.html"


class TypeDetailView(DetailView):
    model = TaskType
    template_name = "tasks/type/detail.html"
    context_object_name = 'type'


class TypeCreateView(CreateView):
    template_name = "tasks/type/create.html"
    form_class = CreateTaskTypeForm


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self) :
        return reverse_lazy('tasks:detail_type', kwargs={'pk': self.object.pk})
    

class TypeUpdateView(UpdateView):
    model = TaskType
    fields = ('name','description', 'is_active')
    template_name = "tasks/type/update.html"

    def get_success_url(self) :
        return reverse_lazy('tasks:detail_type', kwargs={'pk': self.object.pk})


class TypeDeleteView(DeleteView):
    model = TaskType
    template_name = "tasks/type/delete.html"
    success_url = reverse_lazy("tasks:list_type")


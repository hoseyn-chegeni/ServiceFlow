from django.shortcuts import HttpResponseRedirect
from django_filters.views import FilterView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages 
# Create your views here.

class BaseListView(LoginRequiredMixin, PermissionRequiredMixin, FilterView):
    def get_paginate_by(self, queryset):
        # Get the value for paginate_by dynamically (e.g., from a form input or session)
        # Example: Set paginate_by to a user-selected value stored in session
        user_selected_value = self.request.session.get(
            "items_per_page", 10
        )  # Default to 10
        return user_selected_value
    


class BaseDeleteView(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
     message = ''
     def get(self, request, *args, **kwargs):
        # Get the object to be deleted
        self.object = self.get_object()

        # Perform the delete operation directly without displaying a confirmation template
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(
                self.request, self.message
            )
        return HttpResponseRedirect(success_url)

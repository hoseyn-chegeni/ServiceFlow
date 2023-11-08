import csv
from django.http import HttpResponse
from openpyxl import Workbook
from django.urls import reverse_lazy
from django.views import View
from django_filters.views import FilterView
from django.views.generic import DetailView, CreateView, DeleteView
from django.views.generic.edit import UpdateView
from .filters import MyCreatedMeetingsFilter, InvitedMeetingsFilter
from .models import Meetings
from .forms import CreateMeetingsForm


# Create your views here.
class InvitedMeetings(FilterView):
    model = Meetings
    filterset_class = InvitedMeetingsFilter
    template_name = "meetings/invited_meetings.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(attendees=self.request.user)


class MyCreatedMeetings(FilterView):
    model = Meetings
    filterset_class = MyCreatedMeetingsFilter
    template_name = "meetings/my_created_meetings.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(organizer_id=self.request.user.id)


class MeetingDetailView(DetailView):
    model = Meetings
    template_name = "meetings/detail.html"


class CreateMeetingsView(CreateView):
    template_name = "meetings/create.html"
    form_class = CreateMeetingsForm
    success_url = reverse_lazy("index:home")

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)


class DeleteMeetings(DeleteView):
    model = Meetings
    success_url = reverse_lazy("index:home")
    template_name = "meetings/delete.html"


class UpdatedMeetings(UpdateView):
    model = Meetings
    fields = (
        "title",
        "description",
        "date_time",
        "duration",
        "location",
        "attendees",
        "action",
    )
    success_url = reverse_lazy("index:home")
    template_name = "meetings/update.html"


class MeetingsExcelReportView(View):
    def get(self, request, *args, **kwargs):
        # Create a new Excel workbook
        wb = Workbook()
        ws = wb.active

        # Add headers to the Excel file
        ws.append(["title", "description", "organizer", "action"])

        # Query the User model and add data to the Excel file
        meetings = Meetings.objects.all()
        for meet in meetings:
            ws.append(
                [
                    meet.meeting,
                    meet.title,
                    meet.description,
                    meet.organizer.email,
                    meet.action,
                ]
            )

        # Save the workbook to a response object
        response = HttpResponse(content_type="application/ms-excel")
        response["Content-Disposition"] = 'attachment; filename="Meeting_report.xlsx"'
        wb.save(response)

        return response


class MeetingsCSVReportView(View):
    def get(self, request, *args, **kwargs):
        # Create a CSV response object
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="meetings_report.csv"'

        # Write CSV data to the response object
        writer = csv.writer(response)
        writer.writerow(["title", "description", "organizer", "action"])
        meeting = Meetings.objects.all()
        for meet in meeting:
            writer.writerow(
                [
                    meet.meeting,
                    meet.title,
                    meet.description,
                    meet.organizer.email,
                    meet.action,
                ]
            )

        return response
    


class MeetingDetailExcelReportView(View):
    def get(self, request, user_id, *args, **kwargs):
        # Create a new Excel workbook
        wb = Workbook()
        ws = wb.active

        # Add headers to the Excel file
        ws.append(["title", "description", "organizer", "action"])

        # Query the User model for the specific user and add data to the Excel file
        meet = Meetings.objects.get(pk=user_id)
        ws.append([
            meet.meeting,
            meet.title,
            meet.description,
            meet.organizer.email,
            meet.action,
            ])

        # Save the workbook to a response object
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename="{meet.meeting}_report.xlsx"'
        wb.save(response)

        return response

class MeetingDetailCSVReportView(View):
    def get(self, request, user_id, *args, **kwargs):
        # Create a CSV response object
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="meetings_report.csv"'

        # Write CSV data to the response object
        writer = csv.writer(response)
        writer.writerow(["title", "description", "organizer", "action"])
        meet = Meetings.objects.get(pk=user_id)
        writer.writerow([
            meet.meeting,
            meet.title,
            meet.description,
            meet.organizer.email,
            meet.action,
            ])

        return response


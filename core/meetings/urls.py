from django.urls import path
from .views import (
    MyCreatedMeetings,
    InvitedMeetings,
    MeetingDetailView,
    CreateMeetingsView,
    DeleteMeetings,
    UpdatedMeetings,
    MeetingsExcelReportView,
    MeetingsCSVReportView,
    MeetingDetailCSVReportView,
    MeetingDetailExcelReportView,
    CloseMetingView,
    CancelMetingView,
)

app_name = "meetings"

urlpatterns = [
    path("invited_meetings/", InvitedMeetings.as_view(), name="invited_meetings"),
    path(
        "my_created_meetings/", MyCreatedMeetings.as_view(), name="my_created_meetings"
    ),
    path("detail/<int:pk>", MeetingDetailView.as_view(), name="detail"),
    path("create/", CreateMeetingsView.as_view(), name="create"),
    path("delete/<int:pk>/", DeleteMeetings.as_view(), name="delete"),
    path("update/<int:pk>/", UpdatedMeetings.as_view(), name="update"),
    path("close/<int:pk>/", CloseMetingView.as_view(), name="close"),
    path("cancel/<int:pk>/", CancelMetingView.as_view(), name="cancel"),
    # REPORT
    path("excel-report/", MeetingsExcelReportView.as_view(), name="excel_report"),
    path("csv-report/", MeetingsCSVReportView.as_view(), name="csv_report"),
    path(
        "excel-report/<int:user_id>/",
        MeetingDetailExcelReportView.as_view(),
        name="detail_excel_report",
    ),
    path(
        "csv-report/<int:user_id>/",
        MeetingDetailCSVReportView.as_view(),
        name="detail_csv_report",
    ),
]

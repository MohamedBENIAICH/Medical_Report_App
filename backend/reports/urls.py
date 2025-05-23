from django.urls import path
from .views import ReportViewSet, GenerateReportView, SendReportEmailView, send_whatsapp_message

urlpatterns = [
    path('', ReportViewSet.as_view({'get': 'list'}), name='report-list'),
    path('<int:pk>/', ReportViewSet.as_view({'get': 'retrieve'}), name='report-detail'),
    path('generate/', GenerateReportView.as_view(), name='report-generate'),
    path('send-email/', SendReportEmailView.as_view(), name='report-send-email'),
    path('send-whatsapp/', send_whatsapp_message, name='send-whatsapp'),
]
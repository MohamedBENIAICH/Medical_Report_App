from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'image', 'diagnosis', 'details', 'accuracy', 'recommendations', 'language', 'created_at']
        read_only_fields = ['id', 'created_at']


class ReportGenerateSerializer(serializers.Serializer):
    image = serializers.ImageField(required=True)
    language = serializers.CharField(required=False, default='en')


class ReportExportSerializer(serializers.Serializer):
    format = serializers.ChoiceField(choices=['pdf', 'docx', 'txt'])


class ReportEmailSerializer(serializers.Serializer):
    report_id = serializers.UUIDField(required=True)
    patient_email = serializers.EmailField(required=True)
    patient_name = serializers.CharField(required=True)
    format = serializers.ChoiceField(choices=['pdf', 'docx'])
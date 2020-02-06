from rest_framework import serializers

from apps.accounts.api.serializers import UserSerializer
from apps.blog.models import Job,Applicant 


class JobSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = "__all__"


class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = "__all__"

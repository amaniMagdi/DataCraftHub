from rest_framework import serializers
from .models import *

class ServiceRequestSerializer(serializers.ModelSerializer):
    
    lbr_rate = serializers.ReadOnlyField()
    work_day = serializers.ReadOnlyField()

    class Meta:
        model = ServiceRequest
        fields = '__all__'

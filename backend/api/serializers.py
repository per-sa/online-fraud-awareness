from rest_framework import serializers
from .models import *

class FraudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fraud
        fields = '__all__'


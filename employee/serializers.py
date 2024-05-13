from rest_framework import serializers
from .models import empmodel

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=empmodel
        fields="__all__"


    
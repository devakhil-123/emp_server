from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import EmpSerializer
from .models import empmodel


# Create your views here.

class employeeView(ModelViewSet):
    serializer_class=EmpSerializer
    queryset=empmodel.objects.all()

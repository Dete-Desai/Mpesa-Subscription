from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import *
from .models import *
import secrets

# Create your views here.

class CodeViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all().order_by('msisdncode')
    serializer_class = CodeSerializer


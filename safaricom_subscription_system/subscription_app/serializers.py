from rest_framework import serializers
from .models import *

class CodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Code
        fields = ('msisdncode',)


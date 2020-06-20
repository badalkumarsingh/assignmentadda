# serializers.py
from rest_framework import serializers

from .models import Myblog

class MyblogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Myblog
        fields = ('title', 'content')
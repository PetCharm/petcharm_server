# 序列化

from rest_framework import serializers

from myapp.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'email', 'user_icon_url']


class TracePathSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TracePath
        fields = ['trace_path_id', 'trace_path_coordinates',
                  'trace_path_start_time', 'trace_path_end_time', 'trace_path_note']

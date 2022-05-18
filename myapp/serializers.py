# 序列化

from rest_framework import serializers

from myapp.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'email', 'user_icon_url']

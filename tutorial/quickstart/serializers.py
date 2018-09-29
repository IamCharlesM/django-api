from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Should define the information the user is putting in
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Should define how to group fields
        model = Group
        fields = ('url', 'name')

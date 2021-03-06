from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializers, GroupSerializers



class UserViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializers
    
class GroupViewSet(viewsets.ModelViewSet):
    # API endpoint that allows groups to be viewed or edited
    queryset = Group.objects.all()
    serializer_class = GroupSerializers

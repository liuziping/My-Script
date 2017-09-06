# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API允许查看和编辑 用户
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API允许查看和编辑 组
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

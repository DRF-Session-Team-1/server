from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serilizers import *
from .models import *

# Create your views here.
class TodoViewSet(ModelViewSet):
    queryset=Todo.objects.all()
    serializers_class=TodoSerializers
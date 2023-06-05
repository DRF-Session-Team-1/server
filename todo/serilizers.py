from rest_framework.serializers import ModelSerailizers
from .models import *

class TodoSerializers(ModelSerailizers):
    class Meta:
        model = Todo()
        fields = '__all__'
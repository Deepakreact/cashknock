

from rest_framework import serializers
from .models import *


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'

        depth = 1

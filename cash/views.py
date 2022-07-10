from django.shortcuts import render


from .serializers import ProductSerializers


from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def getProducts(request):
    product = Products.objects.all()
    serializer = ProductSerializers(product, many=True)
    return Response(serializer.data)

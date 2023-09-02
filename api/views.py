from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def getData(request):
     category = Category.objects.all()
     serializer = CategorySerializer(category, many=True)
     return Response(serializer.data)
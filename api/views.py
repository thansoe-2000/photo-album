from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import *
from .serializers import *

@api_view(['GET'])
def getPhoto(request):
     photos = Photo.objects.all()
     serializer = PhotoSerializer(Photo, many=True)
     return Response(serializer.data)
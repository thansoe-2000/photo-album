from rest_framework import serializers
from myapp.models import *

class PhotoSerializer(serializers.ModelSerializer):
     class Meta:
          model = Photo
          fields = "__all__"
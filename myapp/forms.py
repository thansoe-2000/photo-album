from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget

class PhotoForm(forms.ModelForm):
   class Meta:
      model = Photo
      fields = "__all__"
      labels = {
         'category':'Category',
         'title':'Title',
         'image':'Image',
         'description':'Description',
      }
      widgets = {
         'category':forms.Select(attrs=({'placeholder':'Select Category'})),
         'description':SummernoteWidget(),
         'title':forms.TextInput(attrs=({'placeholder':'Enter Title'})),
         'image':forms.FileInput(attrs=({})),

      }

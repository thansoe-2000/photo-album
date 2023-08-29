from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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


class CustomUserCreationForm(UserCreationForm):
   class Meta:
      model = User
      fields = ['username', 'password1', 'password2']



   def __init__(self, *args, **kwargs):
      super(CustomUserCreationForm, self).__init__(*args, **kwargs)
      self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter Username'})
      self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter Password'})
      self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Confirm your password'})

class CategoryForm(forms.ModelForm):
   class Meta:
      model = Category
      fields = ['name', 'user']
      labels = {
         'name':'Name',
         'user':'User'
      }
      widgets = {
         'name':forms.TextInput(attrs=({'placeholder':'Create new category', 'class':'form-control'})),
         

      }
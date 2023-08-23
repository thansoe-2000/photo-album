from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def gallary(request):
     categories = Category.objects.all()
     photos = Photo.objects.all()
     context = {
          'categories':categories,
          'photos':photos
     }
     return render(request, 'photos/gallary.html', context)

def viewPhoto(request, pk):
     photo = Photo.objects.get(id=pk)
     context = {
          'photo':photo
     }
     return render(request, 'photos/photo.html', context)

def addPhoto(request):
     form = PhotoForm()
     if request.method == 'POST':
          form = PhotoForm(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               return redirect('gallary')
     context = {
          'form':form
     }
     return render(request, 'photos/add.html', context)
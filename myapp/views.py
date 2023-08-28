from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def loginPage(request):
     return render(request, 'photos/login_register.html')

def gallary(request):
     category = request.GET.get('category')
     if category == None:
          photos = Photo.objects.all()
     else:
          photos = Photo.objects.filter(category__name=category)

     categories = Category.objects.all()
     
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
     categories = Category.objects.all()
     form = PhotoForm()
     if request.method == 'POST':
          form = PhotoForm(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               return redirect('gallary')
     context = {
          'form':form,
          'categories':categories
     }
     return render(request, 'photos/add.html', context)


def check():
   pass

def error_500(request):
   return render(request, 'photos/500_error.html' )
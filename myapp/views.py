from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def loginUser(request):
     page = 'login'

     if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']

          user = authenticate(request, username=username, password=password)
          if user is not None:
               login(request, user)
               return redirect('gallary')
               
     return render(request, 'photos/login_register.html', {'page':page})


def logoutUser(request):
     logout(request)
     return redirect('login')


def registerUser(request):
     page = 'register'
     form = CustomUserCreationForm()
     if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
               user = form.save(commit=False)
               user.save()
               user = authenticate(request, username=user.username, password=request.POST['password1'])
               
               if user is not None:
                    login(request, user)
                    return redirect('gallary')
     context = {
          'form':form,
          'page':page
     }
     return render(request, 'photos/login_register.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def viewPhoto(request, pk):
     photo = Photo.objects.get(id=pk)
     context = {
          'photo':photo
     }
     return render(request, 'photos/photo.html', context)

@login_required(login_url='login')
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
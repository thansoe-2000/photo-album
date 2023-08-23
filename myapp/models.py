from django.db import models

# Create your models here.
class Category(models.Model):
     name = models.CharField(max_length=100,   null=False, blank=False)

     def __str__(self):
          return self.name

class Photo(models.Model):
     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
     title = models.CharField(max_length=100, null=True, blank=True)
     image = models.ImageField(null=False, blank=False)
     description = models.TextField()
     created=models.DateTimeField(auto_now=True,null=True)
     updated=models.DateTimeField(auto_now=True,null=True)
     def __str__(self):
          return self.description
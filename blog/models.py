from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25,unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    head_image = models.ImageField(upload_to='blog/%y/%m/%d/',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return '/blog/{}'.format(self.pk)







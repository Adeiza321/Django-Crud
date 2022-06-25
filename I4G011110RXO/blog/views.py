from dataclasses import fields
from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy

from I4G011110RXO.blog.models import Post

# Create your views here.
class postlistview:
    model= Post

class postcreateview:
    model= Post
    fields = "__all__"
    success_url = reverse_lazy ("blog:all")

class postdetailview:
    model= Post

class postupdateview:
    model= Post
    fields= "__all__"
    success_url= reverse_lazy("blog:all")

class postdeleteview:
    model=Post
    fields="__all__"
    success_url= reverse_lazy("blog:all")

    





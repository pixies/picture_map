from django.shortcuts import render
from .models import Post
# Create your views here.

def lista_de_posts(request):
	posts = Post.objects.all()
	return render(request,'lista_de_posts.html',{'posts':posts})
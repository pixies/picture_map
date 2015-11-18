from django.shortcuts import render
from models import Picture
# Create your views here.
def index(request):
	pictures = Picture.objects.all()
	return render(request,'index.html', {'pictures':pictures})
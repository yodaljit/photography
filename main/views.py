from django.shortcuts import render
from .models import Photo
# Create your views here.
def home(request):
	return render(request, "main/index.html", {})

def about(request):
	return render(request, "main/about.html", {})

def gallery(request):
	photos = Photo.objects.all()
	return render(request, "main/gallery.html", {"photos": photos})

def contact(request):
	return render(request, "main/contact.html", {})

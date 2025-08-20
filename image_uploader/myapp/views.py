from django.shortcuts import render,redirect
from .forms import ImageUploaderForm
from .models import ImageUploader
# Create your views here.

def home(request):
    if request.method == "POST":
        form = ImageUploaderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageUploaderForm()
    # to show all the images on the screen
    img = ImageUploader.objects.all()

    return render(request,'home.html',{'img':img, 'form':form})
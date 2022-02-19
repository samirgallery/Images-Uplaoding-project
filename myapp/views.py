from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.
def index (request):
    if request.method == "POST":
        form =ImageForm(request.POST ,request.FILES)
        if form.is_valid():
          form.save()
    form = ImageForm()
    img=Image.objects.all()
    return render (request,'myapp/index.html',{'img':img,'form':form})

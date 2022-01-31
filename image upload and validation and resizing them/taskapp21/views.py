from django.shortcuts import  render
from django.core.files.storage import FileSystemStorage
from PIL import Image
from .models import MyModel

def dummy(request):
    return render(request, 'taskapp21/upload.html')
def upload(request):
    if request.method == 'POST':
        if request.FILES['upload'] or None:
        
            upload = request.FILES['upload']
            print("++++++++++++++++++++size of original++++++++++++++++++++++++++",upload.size)
            print("______________________________________________________________",upload)
            data=MyModel(photo=upload)
            data.save()
            print("***************************data inserted**********************************",data)
        else:
         return render(request, 'taskapp21/upload.html')
       
    else:
         return render(request, 'taskapp21/upload.html')
        
    return render(request, 'taskapp21/upload.html')

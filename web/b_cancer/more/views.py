from django.shortcuts import render
from django.http import HttpResponse
from .models import info
from .forms import TumorForm
from .ml import predict

def more(request):
    infos=info.objects.all()
    return render(request,'file\more_info.html',{'infos':infos})
# Create your views here.


def upload_image(request):
    if request.method == "POST":
        # info.objects.all().delete()
        form=TumorForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save()
            instance_path=instance.image.path
            # image = request.FILES['image']    
            prediction=predict.predict_img(instance_path)
            instance.Tumer=prediction
            instance.save()
            if prediction =="benign":
                discription='''Benign: Refers to a tumor or growth that is non-cancerous, grows slowly, and does not spread to other parts of the body.
                 Usually, it is less harmful and can often be removed surgically.'''
            elif prediction=='malignant':
                discription='''Malignant: Refers to a tumor or growth that is cancerous, can grow rapidly, invade nearby tissues, and spread (metastasize) to other parts of the body.
                  Malignant tumors are more dangerous and may require aggressive treatment like surgery, chemotherapy, or radiation.'''
            else:
                discription='Congratulation, You are healthy. Wishing you long and healthy life.'

                
            return render(request, 'file\\ans.html',{'prediction':prediction,'dis':discription})
        
    else:
        form = TumorForm()
    
    return render(request, 'file\\upload.html', {
        'form': form})
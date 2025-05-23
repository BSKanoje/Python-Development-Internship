from django.shortcuts import render, redirect
import uuid 
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link= url,uuid=uid)
        new_url.save()
        return HttpResponse(uid)
    
# def go(request, pk):
#     url_details = Url.objects.get(uuid=pk)
#     return redirect('https://'+url_details.link)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    if url_details.link.startswith("www"):
        return redirect('https://'+url_details.link)
    elif url_details.link.startswith("https://"):
        return redirect(url_details.link)
    else:
        return redirect('https://www.'+url_details.link)
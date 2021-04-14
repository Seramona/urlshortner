from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse
import re

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link0 = request.POST['link']
        url = re.compile(r"https?://")
        link = url.sub('', link0).strip().strip('/')
        uid = str(uuid.uuid4())[:5] # выдаём уникальный идентификатор с сокращением до 5 символов
        new_url = Url(link=link,uuid=uid) # выбрали данные
        new_url.save() # внесли в базу
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk) # ищем объект в БД с uuid
    return redirect('https://'+url_details.link) # перенаправляем по ссылке объекта из БД
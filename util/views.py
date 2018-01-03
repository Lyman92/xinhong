from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
# from django.views.decorators.csrf import csrf_exempt

from xinhong.slider.models import Slider


# Create your views here.
def index(request, method):
    context = {}
    template_name = ''
    if method == '':
        try:
            slider = Slider.objects.all()[0]
            context['title'] = slider.name
        except:
            context['title'] = ''
        template_name = 'util/util.html'
    return render(request, template_name, context)


# @csrf_exempt
def setFlash(request):
    print('===================')
    if request.method == 'POST':
        try:
            slider = Slider.objects.all()[0]
            slider.name = request.POST['title']
            slider.expiry_date = date.today()
            slider.image = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1514999144106&di=bf3c6650e112c6a610181b908e7545eb&imgtype=0&src=http%3A%2F%2Fimg.800.cn%2F2015%2F01%2F23%2Fn_54c210a37894d.jpg'
            slider.save()
        except:
            slider = Slider()
            slider.name = request.POST['title']
            slider.expiry_date = date.today()
            slider.image = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1514999144106&di=bf3c6650e112c6a610181b908e7545eb&imgtype=0&src=http%3A%2F%2Fimg.800.cn%2F2015%2F01%2F23%2Fn_54c210a37894d.jpg'
            slider.save()
        return index(request,'')

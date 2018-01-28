import json

from django.shortcuts import render
from .models import Product
from xinhong.slider.models import Slider
from xinhong.helpers import Helpers


def index(request):
    context = {'title': ''}
    product_set = None
    arr_img = []
    try:
        product_set = Product.objects.all()
        for item in product_set:
            arr_img.append(Helpers.get_cloud_file_url(item.img_bg))
    except:
        pass
    context['products'] = product_set
    context['imgs'] = arr_img
    return render(request, 'main/index.html', context)


def product_content(request, id):
    context = {'': ''}
    product = Product()
    contents = []
    structure = []  # 数组值为0是图片,为1是文字
    try:
        product = Product.objects.filter(id=id)[0]
    except:
        pass
    str = product.contents
    try:
        contents = json.loads(str)
        for index in range(0, len(contents)):
            if Helpers.is_img_string(contents[index]):
                contents[index] = Helpers.get_cloud_file_url(contents[index])
                structure.append(0)
            else:
                structure.append(1)
    except:
        pass
    print(structure)
    context['contents'] = contents
    context['structure'] = structure
    return render(request, 'main/main_product_content.html', context)


def welcome(request):
    context = {'title': ''}
    slider = Slider()
    try:
        slider = Slider.objects.all()[0]
    except:
        pass
    context['title'] = slider.name
    context['img'] = Helpers.get_cloud_file_url(slider.image)
    return render(request, 'main/welcome.html', context)


def contact_us(request):
    return render(request, 'main/main_contact_us.html')

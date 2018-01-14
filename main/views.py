from django.shortcuts import render
from .models import Product
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
    print(arr_img)
    return render(request, 'main/index.html', context)

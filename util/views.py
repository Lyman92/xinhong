from django.shortcuts import render
from datetime import date

from xinhong.slider.models import Slider
from main.models import Product
from .forms import UploadFileForm, EditProductForm
from xinhong.helpers import Helpers


# Create your views here.
def index(request):
    context = {'title': '首页'}
    slider = Slider()
    uploadFileForm = UploadFileForm()
    if request.method == 'GET':
        try:
            slider = Slider.objects.all()[0]
            uploadFileForm = UploadFileForm({'title': slider.name})
        except:
            pass
    else:
        uploadFileForm = UploadFileForm(request.POST, request.FILES)
        try:
            slider = Slider.objects.all()[0]
        except:
            pass
        print(uploadFileForm.errors)
        if uploadFileForm.is_valid():
            slider.name = request.POST['title']
            slider.expiry_date = date.today()
            slider.upload_welcome_image(request.FILES['image'])
            print(request.FILES['image'])
            slider.save()
    image = Helpers.get_cloud_file_url(slider.image)
    context['title'] = slider.name
    context['uploadFileForm'] = uploadFileForm
    context['image'] = image
    return render(request, 'util/util.html', context)


def products(request):
    context = {'': ''}
    ary_products = []
    try:
        ary_products = Product.objects.all()
    except:
        pass
    context['products'] = ary_products
    return render(request, 'util/products.html', context)


def edit_product(request):
    context = {'': ''}
    form = EditProductForm()
    product = Product()
    product_id = -1
    msg = ''
    if request.method == 'GET':
        try:
            product_id = request.GET['id']
        except:
            pass
        if product_id != -1:  # 原有数据
            product_set = Product.objects.filter(id=product_id)
            data = {'': ''}
            if len(product_set) == 1:
                product = product_set[0]
                data = {'title_big': product.title_big,
                        'title_after_big': product.title_after_big,
                        'title_small': product.title_small,
                        'ordering': product.ordering}
            form = EditProductForm(data)
    else:  # POST
        form = EditProductForm(request.POST, request.FILES)
        product_id = request.POST['id']
        is_update = False
        if product_id != -1:  # 修改
            try:
                product = Product.objects.filter(id=product_id)[0]
                is_update = True
            except:
                pass
        if form.is_valid():
            product.title_big = request.POST['title_big']
            product.title_after_big = request.POST['title_after_big']
            product.title_small = request.POST['title_small']
            try:
                product.upload_img_bg(request.FILES['img_bg'], 'p-%s.jpg' % product_id)
            except:
                pass
            product.link = 'link'
            if request.POST['ordering'] != '':
                product.ordering = request.POST['ordering']
            product.save()
            if is_update:
                msg = '修改成功!'
            else:
                msg = '添加成功!'
    context['form'] = form
    context['id'] = product_id
    context['img_bg'] = Helpers.get_cloud_file_url(product.img_bg)
    context['msg'] = msg
    return render(request, 'util/edit_product.html', context)

from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(label='顶部标题', max_length=50)
    image = forms.FileField()


# 编辑产品表单
class EditProductForm(forms.Form):
    title_big = forms.CharField(label='大标题', max_length=50)
    title_after_big = forms.CharField(label='标题下标（选填，显示在大标题右下角，字体同小标题）', max_length=50, required=False)
    title_small = forms.CharField(label='小标题', max_length=50)
    img_bg = forms.ImageField(label='背景图片', required=False)
    link = forms.HiddenInput()
    ordering = forms.IntegerField(label='产品序号（选填,不填排将在最前）', required=False)

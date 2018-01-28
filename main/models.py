from django.db import models
from xinhong.helpers import Helpers


# Create your models here.
class Product(models.Model):
    title_big = models.CharField(max_length=50)
    title_after_big = models.CharField(max_length=50, default='')
    title_small = models.CharField(max_length=50, default='')
    img_bg = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    ordering = models.IntegerField(default=1)
    contents = models.CharField(max_length=4096, default='')

    def __str__(self):
        return self.title_big

    def __unicode__(self):
        return u'%s' % self.title_big

    def upload_img_bg(self, file, img_name):
        Helpers.upload_file(file, img_name)
        self.img_bg = img_name

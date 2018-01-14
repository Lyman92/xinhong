from django.db import models
from xinhong.helpers import Helpers


# Create your models here.
class Slider(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    expiry_date = models.DateField()
    ordering = models.IntegerField(default=1)
    link = models.CharField(blank=True, null=True, max_length=200)
    welcome_img_name = 'xinhong_welcome.png'

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ['ordering', 'expiry_date']

    def upload_welcome_image(self, file):
        Helpers.upload_file(file, self.welcome_img_name)
        self.image = self.welcome_img_name

from django.db import models


# Create your models here.
class Slider(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    expiry_date = models.DateField()
    ordering = models.IntegerField(default=1)
    link = models.CharField(blank=True, null=True, max_length=200)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ['ordering', 'expiry_date']

from django.db import models
from .utils import code_generator,create_shortcode

class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15,unique=True,blank=True) #non nullable if then
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(KirrURL,self).save(*args,**kwargs)

    def __str__(self): #show the url instead of kirrurl or name
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

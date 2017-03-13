from django.db import models

class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15,unique=True) #non nullable if then
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self): #show the url instead of kirrurl or name
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

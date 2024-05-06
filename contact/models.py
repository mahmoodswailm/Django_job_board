from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=20,blank=True,null=True)
    place = models.CharField(max_length=30)
    phone = models.CharField(max_length=(20))
    email = models.EmailField(max_length=50)
    
    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")
        
# Create your models here.

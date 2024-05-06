from typing import Iterable
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

"""
Django model feild:
    - html widget
    - validation
    - db size
"""
JOB_TYPE = (("Full Time","Full Time"),
                ("Part Time","Part Time"))

# func to upload images instead 
def Upload_Image(instance,filename:str):
    image_name,extention= filename.split('.')
    
    return "jobs/%s.%s"%(instance.id,extention)


class Job(models.Model): #this a model represent db tabel 
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=20) # column fr
    
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    Description = models.TextField(max_length=1000) # for long text
    Published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=2000)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)#CASCADE = >on delete will delete evrything related to job
    image = models.ImageField(upload_to= Upload_Image)# can insert 'jobs/' as value or the func that you wrote
    slug = models.SlugField(blank=True,null=True) #to show job title in headline bar
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)
    
    
    def __str__(self) -> str: #to show the job name instead of job oject1
        return self.title


class Category(models.Model):
    name = models.CharField((""), max_length=50)
    
    def __str__(self) -> str: #to show the Category name instead of Category oject1
        return self.name
    

class Apply(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    name =models.CharField(max_length=20)
    Email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to="apply/")
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


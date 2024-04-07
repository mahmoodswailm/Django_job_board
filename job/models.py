from django.db import models

# Create your models here.

"""
Django model feild:
    - html widget
    - validation
    - db size
"""
JOB_TYPE = (("Full Time","Full Time"),
                ("Part Time","Part Time"))
class Job(models.Model): #this a model represent db tabel 
    title = models.CharField(max_length=20) # column fr
    
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    Description = models.TextField(max_length=1000) # for long text
    Published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=2000)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)#CASCADE = >on delete will delete evrything related to job
    def __str__(self) -> str: #to show the job name instead of job oject1
        return self.title


class Category(models.Model):
    name = models.CharField((""), max_length=50)
    
    def __str__(self) -> str: #to show the Category name instead of Category oject1
        return self.name
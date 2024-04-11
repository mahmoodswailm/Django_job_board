from django.shortcuts import render
from .models import Job
# Create your views here.
def job_lists(request,id):
    job_lists = Job.objects.all() # => return all objects in Job
    return render(request,'job/job_lists.html')#(request,templates (path),context)

def job_detail(request):
    pass
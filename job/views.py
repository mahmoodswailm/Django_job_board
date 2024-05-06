from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from .models import Job
from .form  import ApllyForm,Add
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filter import JobFilter



# Create your views here.
def job_lists(request):
    job_lists1 = Job.objects.all() # => return all objects in Job
    
    my_filter = JobFilter(request.GET,queryset=job_lists1)
    
    job_lists = my_filter.qs
    
    paginator = Paginator(job_lists,4)  # Show 3 contacts per page.
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {"jobs":page_obj,"job":job_lists1,"myfilter":my_filter}
    # print(job_lists)
    return render(request,'job/job_lists.html',context) #=> (request,templates (path),context)



def job_detail(request,slug):   # using slug instead of id 
    job_detail = Job.objects.get(slug=slug)    #id=id
    if request.method == "POST" :
        form = ApllyForm(request.POST,request.FILES)
        
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            
            
            
    
    else:
        form = ApllyForm()
    
    
    context = {"job":job_detail,"form":form}
    return render(request,"job/job_detail.html",context)


@login_required
def add_job(request):
    
    if request.method == "POST":
        form = Add(request.POST,request.FILES)
        if form.is_valid():
            # form.save(commit=False)
            # form.save(commit=False).owner = request.user
            # form.save(commit=False).save()
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            
            return redirect(reverse("jobs:job_list")) # to return to job_list page
            
        ...
    else:
        form=Add()

    context = {"form":form}
    return render(request,"job/add_job.html",context)
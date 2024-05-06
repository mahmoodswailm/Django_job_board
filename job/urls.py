from django.urls import path
from . import views

app_name= 'job'

urlpatterns = [ # i forgot to type s in urlpatterns aaaaaaaaaaah
    path('',views.job_lists,name="job_list"),# get all objects (jobs) instantiated form Class job
    path('add',views.add_job,name="add_job"),
    path('<str:slug>',views.job_detail,name='job_detail') # get details of specific job with id
    # using slug instead of id 
]

from django.urls import path,include
from . import views
urlpattern = [
    path('<int:id>',views.job_detail),
    path('',views.job_lists)
    
]
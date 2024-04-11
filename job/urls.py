from django.urls import path
from . import views
urlpatterns = [ # i forgot to type s in urlpatterns aaaaaaaaaaa
    path('',views.job_lists),
    path('<int:id>',views.job_detail)
]

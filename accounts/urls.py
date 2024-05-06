from django.urls import path
from . import views
app_name= "accounts"

urlpatterns = [
    path("signup",views.signup,name ="signup"),
    path("Profile",views.profile,name ="Profile"),
    path("Profile/edit",views.Profile_edit,name ="Profile_edit")
]

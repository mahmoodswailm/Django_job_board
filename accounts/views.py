from django.shortcuts import render,redirect
from .form import SignForm,UserForm,ProfileForm
from .models import Profile
from django.contrib.auth import authenticate,login
from django.urls import reverse

# Create your views here.
def signup(request):
    
    if request.method =="POST":
        form = SignForm(request.POST)
        print("hi")
        if form.is_valid():
            print("hi2")
            
            form.save()
            username= form.cleaned_data["username"]
            password= form.cleaned_data["password1"]
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect("/accounts/profile")
    else:
        form = SignForm()
    
    
    return render(request,"registration/signup.html",{"form":form})




def profile(request):
    
    profile = Profile.objects.get(user=request.user)
    
    return render(request,"account/profile.html",{"profile":profile})


def Profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method =="POST":
        userform = UserForm(request.POST,request.FILES,instance=request.user)
        profileform= ProfileForm(request.POST,request.FILES,instance=profile)
        print("hi")
        if userform.is_valid() and profileform.is_valid():
            print("hi")
            userform.save()
            myprofile = profileform.save(commit= False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse("accounts:Profile"))
    else:
        userform = UserForm(instance=request.user)
        profileform= ProfileForm(instance=profile)
    context = {"userform":userform,"profileform":profileform}
    
    return render(request,"account/profile_edit.html",context=context)


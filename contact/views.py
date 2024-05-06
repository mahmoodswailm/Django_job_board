from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings #to import setting of the project
from django.http import HttpResponse
# Create your views here.
def handler404(request,exception):
    return HttpResponse("404; page not found")


def send_message(request):
    info = Info.objects.first()
    
    if request.method == "POST":
        subject = request.POST["subject"]
        email = request.POST["email"]
        # name = request.POST["name"]
        msg = request.POST["message"]
        print(subject) # to check if form work or not
        print(email)
        # print(name)
        print(msg)
        send_mail(
                subject,
                msg,
                settings.EMAIL_HOST_USER,
                [email],
                # fail_silently=False,
                )
    
    context = {"myinfo":info}
    
    return render(request,"contact_page/page.html",context)
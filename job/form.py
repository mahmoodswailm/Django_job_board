from django import forms
from .models import Apply,Job




class ApllyForm(forms.ModelForm): # it inherit from Modelform be we deal with
    # a form that we've created  model for 
    class Meta:
        model = Apply
        fields = ["name","Email","website","cv",'cover_letter']



class Add(forms.ModelForm):
    class Meta:
        model = Job
        # fields = ['title','job_type','Description','vacancy','salary','experience','category','image']
        fields = "__all__" # to get all attributes in Job class
        exclude = ("published_at","slug","owner",'image') #to exclude from fields
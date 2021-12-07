from django import forms
from django.forms import formsets
from grups.models import *

class NameForm ( formsets.Form ) :
    your_name = forms.CharField(label = "your name" , max_length=10)

class SimpleForm(forms.Form):
    name = forms.CharField(max_length=255,label="نام",initial="maktab",)
    lastname = forms.CharField(max_length=255,label="نام خانوادگی ",help_text="نام خانوادگی منظور همون فامیلی است ",initial="sharif")
    birthday = forms.IntegerField(label="سال تولد ") #required=False,    error_messages={'invalid':"داداش فقط عدد"}
    choice = forms.ChoiceField(label="الکی",choices=((1,'one'),(2,'two')))
    description = forms.CharField(widget=forms.Textarea)
    tags = forms.ModelChoiceField(label=" model choice",queryset=Tag.objects.all()) #to_field_name = "title" --> chose value of select
    #refrence : https://docs.djangoproject.com/en/3.2/ref/forms/fields/#django.forms.ModelChoiceField

    def save(self):
        print('on save method : ',self.cleaned_data)
        # ....
        #refrence : https://stackoverflow.com/questions/11943912/how-do-you-write-a-save-method-for-forms-in-django


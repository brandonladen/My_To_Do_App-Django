from django import forms
from .models import To_Do_List

class To_Do_List_Form(forms.ModelForm):
    class Meta:
        model = To_Do_List
        #fields = ['Title', 'Description', 'user']
        exclude = ['user']
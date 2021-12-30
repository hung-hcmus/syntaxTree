from django import forms
from django.forms import ModelForm

from .models import input_text

# Create an inputform
class InputForm(ModelForm):
    class Meta:
        model = input_text
        fields = "__all__"
        labels ={
            'text': ''
        }
        widgets = {
            'text' : forms.TextInput(attrs={'class':'form__field', 'placeholder':'Name', 'name':'name', 'id':'name'}),
        }


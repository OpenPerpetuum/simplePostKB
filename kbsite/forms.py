from django import forms
from models import Kill_PureText

class KillForm(forms.ModelForm):
    class Meta:
        model = Kill_PureText
        fields = ["content"]
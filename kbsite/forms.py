from django import forms
from models import Kill_PureText, Kill

class KillFormText(forms.ModelForm):
    class Meta:
        model = Kill_PureText
        fields = ["content"]

class KillForm(forms.ModelForm):
    class Meta:
        model = Kill
        exclude = []

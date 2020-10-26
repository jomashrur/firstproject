
from django import forms


class shakForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    views = forms.IntegerField()
    date = forms.DateField(widget=forms.SelectDateWidget)

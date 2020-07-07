from django import forms

class AnalysisForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    image = forms.ImageField()

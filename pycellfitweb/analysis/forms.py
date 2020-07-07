from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class ParametersForm(forms.Form):
    name = forms.CharField(max_length=100)
    base64_image = forms.CharField(max_length=100000000)

from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField(label='Upload Task\'s File')
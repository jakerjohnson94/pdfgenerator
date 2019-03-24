from django import forms
from pdfgenerator.models import Upload


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ["upload"]


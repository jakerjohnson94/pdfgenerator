from django.db import models
from django.core.files.storage import FileSystemStorage

fs_upload = FileSystemStorage(location="pdfgenerator/media/uploads/")
fs_pdf = FileSystemStorage(location="pdfgenerator/media/pdfs/")


class Upload(models.Model):
    file = models.FileField(storage=fs_upload)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        name = self.file.name.split("/")[-1]
        return name


class Converted_Pdf(models.Model):
    file = models.FileField(storage=fs_pdf)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        name = self.file.name.split("/")[-1]
        return name

